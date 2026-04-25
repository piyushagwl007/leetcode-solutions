from collections import Counter

class Solution:

    def minWindow(self, s: str, t: str) -> str:
       left = 0
       targetMap = Counter(t)
       required = len(targetMap)
       currentCharMap = {}
       minWindowSize = float('inf')
       minLeft = None
       minRight = None
       satisfied = 0
       for right in range(len(s)):
        currentCharMap[s[right]] = currentCharMap.get(s[right], 0) + 1
        if s[right] in targetMap and currentCharMap[s[right]] == targetMap[s[right]]:
            satisfied += 1
        while required == satisfied:
            currentWindowSize = right - left +1
            if currentWindowSize < minWindowSize:
                minWindowSize = currentWindowSize
                minLeft = left
                minRight = right
            currentCharMap[s[left]] -= 1
            if s[left] in targetMap and currentCharMap[s[left]] < targetMap[s[left]]:
                satisfied -= 1
            left += 1
       minSubstring = s[minLeft:minRight+1] if minLeft is not None else ""
       return minSubstring