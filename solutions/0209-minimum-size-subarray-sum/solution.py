class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        minSubArrayLenVal = float('inf')
        sumOfCurrentArray = 0
        for right in range(len(nums)):
            sumOfCurrentArray += nums[right]
            while sumOfCurrentArray >= target:
                minSubArrayLenVal = min(minSubArrayLenVal, right-left + 1)
                sumOfCurrentArray -= nums[left]
                left += 1
        return minSubArrayLenVal if minSubArrayLenVal <= len(nums) else 0