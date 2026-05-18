# Standard library imports that LeetCode's Python judge auto-injects.
# Prepended by github-leetcode-sync so the solution is runnable locally.
from typing import *  # noqa: F401,F403
from collections import *  # noqa: F401,F403
import math  # noqa: F401
import heapq  # noqa: F401
import bisect  # noqa: F401
import functools  # noqa: F401
import itertools  # noqa: F401
import operator  # noqa: F401
import string  # noqa: F401

from solutions.helpers import ListNode, TreeNode  # noqa: F401

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        start, end = intervals[0]
        currentInterval = 0
        for i in range(1, len(intervals)):
            starti, endi = intervals[i]
            if start <= endi and starti <= end:
                start = start
                end = max(end, endi)
            else:
                result.append([start, end])
                start = starti
                end = endi
        result.append([start, end])
        return result