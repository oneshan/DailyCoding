"""
    283 - Move Zeros
    @author oneshan
    @version 1.0 2/7/2017
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for num in nums:
            if num:
                nums[pos] = num
                pos += 1

        for i in range(pos, len(nums)):
            nums[i] = 0
