class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numberOf0 = 0
        numberOf1 = 0
        numberOf2 = 0

        for num in (nums):
            if num == 0:
                numberOf0 += 1
            elif num == 1:
                numberOf1 += 1
            elif num == 2:
                numberOf2 += 1
        i = 0
        while numberOf0 > 0:
            nums[i] = 0
            i += 1
            numberOf0 -= 1
        while numberOf1 > 0:
            nums[i] = 1
            i += 1
            numberOf1 -= 1
        while numberOf2 > 0:
            nums[i] = 2
            i += 1
            numberOf2 -= 1
    