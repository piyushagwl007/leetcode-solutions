"""Runs every parametrized LeetCode case discovered by conftest.py."""

from __future__ import annotations

from typing import Any

import pytest

from solutions.conftest import LeetCodeCase, SOLUTIONS_ROOT, load_solution
from solutions.helpers import UnsupportedTypeError, compare_values, parse_value


def test_harness_loads() -> None:
    """Sentinel test: keeps CI green on a freshly bootstrapped repo before any problems are synced."""
    assert SOLUTIONS_ROOT.exists()


def test_leetcode_solution(leetcode_case: LeetCodeCase) -> None:
    spec = leetcode_case.spec
    case = leetcode_case.case

    function_name = spec.get("functionName")
    if not function_name:
        pytest.skip("no functionName captured")

    expected_raw = case.get("expected")
    if expected_raw is None:
        pytest.skip("no expected output captured")

    params = spec.get("params") or []
    inputs = case.get("input") or []
    if len(inputs) != len(params):
        pytest.skip(f"input/param count mismatch ({len(inputs)} vs {len(params)})")

    parsed_args: list[Any] = []
    for raw, param in zip(inputs, params):
        try:
            parsed_args.append(parse_value(raw, param.get("type")))
        except UnsupportedTypeError as e:
            pytest.skip(str(e))

    return_type = spec.get("returnType")
    try:
        expected = parse_value(expected_raw, return_type)
    except UnsupportedTypeError as e:
        pytest.skip(str(e))

    solution = load_solution(leetcode_case.problem_dir)
    method = getattr(solution, function_name)
    actual = method(*parsed_args)

    assert compare_values(actual, expected, return_type), (
        f"input={inputs!r} expected={expected_raw!r} got={actual!r}"
    )
