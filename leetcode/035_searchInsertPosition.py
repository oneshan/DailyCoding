"""
    035 - Search Insert Position
    @author oneshan
    @version 1.0 2/17/2017
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right + 1) / 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left
