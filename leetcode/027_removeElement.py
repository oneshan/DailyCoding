"""
    027 - Remove Element
    @author oneshan
    @version 1.0 2/11/2017
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[idx] = nums[i]
                idx += 1
        return idx
