"""Pytest collection hook: discovers each problem directory and parametrizes
one case per example input. The actual test functions live in test_solutions.py
(separating them avoids pytest collecting conftest.py as a test module).
"""

from __future__ import annotations

import importlib.util
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator


SOLUTIONS_ROOT = Path(__file__).parent


@dataclass
class LeetCodeCase:
    problem_dir: Path
    spec: dict
    case_index: int
    case: dict


def iter_problems() -> Iterator[Path]:
    for entry in sorted(SOLUTIONS_ROOT.iterdir()):
        if not entry.is_dir():
            continue
        if (entry / "solution.py").exists() and (entry / "tests.json").exists():
            yield entry


def load_solution(problem_dir: Path) -> Any:
    sol_path = problem_dir / "solution.py"
    spec = importlib.util.spec_from_file_location(
        f"solutions.{problem_dir.name}.solution", sol_path
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {sol_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not hasattr(module, "Solution"):
        raise AttributeError(f"{sol_path} has no Solution class")
    return module.Solution()


def _collect_cases() -> list[LeetCodeCase]:
    cases: list[LeetCodeCase] = []
    for problem_dir in iter_problems():
        spec = json.loads((problem_dir / "tests.json").read_text())
        for i, case in enumerate(spec.get("cases", [])):
            cases.append(LeetCodeCase(problem_dir, spec, i, case))
    return cases


def pytest_generate_tests(metafunc):
    if "leetcode_case" not in metafunc.fixturenames:
        return
    cases = _collect_cases()
    metafunc.parametrize(
        "leetcode_case",
        cases,
        ids=[f"{c.problem_dir.name}[{c.case_index}]" for c in cases],
    )
