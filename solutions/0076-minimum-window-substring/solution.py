class Solution:
    def hasAllChars(self, substring:str, t: str):
        for char in t:
            if substring.count(char) < t.count(char):
                return False
        return True

    def hasMatchingCharCountInCharMap(self, sustringCharMap:dict[str], targetCharMap:dict[str]):
        for char, charCount in targetCharMap.items():
            if char not in sustringCharMap or sustringCharMap[char] < charCount:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        minWindowLength = float('inf')
        minWindowLeft = None
        minWindowRight = None
        charMap = {}
        for char in t:
            if char in charMap:
                charMap[char] += 1
            else:
                charMap[char] = 1
 
        # for left in range(len(s)):
        #     currentCharMap = {}
        #     for right in range(left, len(s)):
        #         if s[right] in currentCharMap:
        #             currentCharMap[s[right]] +=1 
        #         else:
        #             currentCharMap[s[right]] = 1
                
        #         # hasMatchingChar = self.hasMatchingCharCountInCharMap(currentCharMap, charMap)
        #         # if hasMatchingChar and minWindowLength > (right - left +1):
        #         #     minWindowLength = min(minWindowLength, right - left +1)
        #         #     minWindowLeft = left
        #         #     minWindowRight = right
        left = 0
        right = 0
        runningSubstring = ""
        runningCharMap = {}
        while right < len(s):
            if s[right] in runningCharMap:
                runningCharMap[s[right]] += 1
            else:
                runningCharMap[s[right]] = 1
            while self.hasMatchingCharCountInCharMap(runningCharMap, charMap):
                currentLength = right - left + 1
                if currentLength < minWindowLength:
                    minWindowLength = min(minWindowLength, right - left +1)
                    minWindowLeft = left
                    minWindowRight = right
                runningCharMap[s[left]] -= 1
                left += 1
            right += 1
        return s[minWindowLeft:minWindowRight+1] if minWindowLeft is not None and minWindowRight is not None else ""
                    
        