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
        merged = True
        while merged:
            result = []
            used= [False] * len(intervals)
            merged = False
            for i in range(len(intervals)):
                if used[i] == True:
                    continue
                starti, endi = intervals[i]
                for j in range(len(intervals)):
                    if i == j or used[j] == True:
                        continue
                    startj, endj = intervals[j]
                    if starti <= endj and startj <= endi:
                        merged = True
                        used[j] = True
                        starti = min(starti, startj)
                        endi = max(endi, endj)
                result.append([starti, endi])
            intervals = result
        return result