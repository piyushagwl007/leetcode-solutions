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
        numberOfDays = len(temperatures)
        output = [ 0 for i in range(numberOfDays)]
        for i in range(numberOfDays -2, -1, -1):
            j = i + 1
            while j < numberOfDays :
                if temperatures[j] > temperatures[i]:
                    output[i] = j - i
                    break
                
                if output[j] == 0:
                    break
                j = j + output[j]
        
        return output