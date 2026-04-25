class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lengthOfSubstr = 0
        left = 0
        charSet = {}
        for right in range(len(s)):
            if s[right] in charSet and left <= charSet[s[right]]:
                left = charSet[s[right]] + 1
            charSet[s[right]] = right
            lengthOfSubstr = max(lengthOfSubstr, right-left+1)
        return lengthOfSubstr