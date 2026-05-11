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
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
       stack = []
       output = [0] * len(temperatures)
       for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                output[index] = i - index
            stack.append(i)
       return output