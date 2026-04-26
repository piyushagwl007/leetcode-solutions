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
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            runningString = ""
            for j in range(i, len(s)):
                runningString = runningString + s[j]
                if runningString == runningString[::-1]:
                    count += 1
        
        return count
