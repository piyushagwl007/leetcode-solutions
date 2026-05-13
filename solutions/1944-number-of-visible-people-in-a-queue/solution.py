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
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack  = []
        n = len(heights)
        output = [0] * n
        for i in range(n-1, -1, -1):
            while stack and stack[-1] < heights[i]:
                stack.pop()
                output[i] += 1
            if stack:
                output[i] += 1
            stack.append(heights[i])
        return output
