"""Type parsing and equality for LeetCode's example test cases.

LeetCode's question metadata declares parameter types as strings like:
    integer, integer[], integer[][], string, string[], boolean, double,
    character, character[][], ListNode, TreeNode, void

For the JSON-serializable subset we just route through json.loads. ListNode
and TreeNode get bespoke parsing/serialization. Anything else raises
UnsupportedTypeError so the test is skipped (not failed) — keeps CI green
for problems with exotic types until we add support.
"""

from __future__ import annotations

import json
import math
from typing import Any, Optional


class UnsupportedTypeError(Exception):
    """Raised when a LeetCode type is not yet handled by the harness."""


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


_JSON_BASES = {
    "integer",
    "long",
    "double",
    "float",
    "string",
    "boolean",
    "character",
    "void",
}


def parse_value(raw: str, type_str: Optional[str]) -> Any:
    """Parse a raw LeetCode input string according to its declared type."""
    if type_str is None:
        return json.loads(raw)

    t = type_str.strip()

    if t.startswith("ListNode"):
        return list_to_listnode(json.loads(raw))
    if t.startswith("TreeNode"):
        return list_to_treenode(json.loads(raw))

    base = t.replace("[]", "").lower()
    if base in _JSON_BASES:
        return json.loads(raw)

    raise UnsupportedTypeError(f"unsupported type: {type_str}")


def list_to_listnode(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def listnode_to_list(node: Optional[ListNode]) -> list[int]:
    out: list[int] = []
    while node is not None:
        out.append(node.val)
        node = node.next
    return out


def list_to_treenode(values: list[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    if values[0] is None:
        return None
    root = TreeNode(values[0])
    queue: list[TreeNode] = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])  # type: ignore[arg-type]
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])  # type: ignore[arg-type]
            queue.append(node.right)
        i += 1
    return root


def treenode_to_list(root: Optional[TreeNode]) -> list[Optional[int]]:
    if root is None:
        return []
    out: list[Optional[int]] = []
    queue: list[Optional[TreeNode]] = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def compare_values(actual: Any, expected: Any, type_str: Optional[str]) -> bool:
    """Compare a solution's return value against the expected output."""
    if type_str is not None:
        t = type_str.strip()
        if t.startswith("ListNode"):
            return listnode_to_list(actual) == (
                expected if isinstance(expected, list) else listnode_to_list(expected)
            )
        if t.startswith("TreeNode"):
            actual_list = actual if isinstance(actual, list) else treenode_to_list(actual)
            expected_list = (
                expected if isinstance(expected, list) else treenode_to_list(expected)
            )
            return actual_list == expected_list
        if t in {"double", "float"}:
            return _floats_equal(actual, expected)

    if isinstance(actual, float) or isinstance(expected, float):
        return _floats_equal(actual, expected)

    return actual == expected


def _floats_equal(a: float, b: float, tol: float = 1e-5) -> bool:
    if math.isnan(a) or math.isnan(b):
        return math.isnan(a) and math.isnan(b)
    return abs(a - b) <= tol
