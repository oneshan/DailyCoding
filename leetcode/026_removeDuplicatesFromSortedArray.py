"""
    026 - Remove Duplicates from Sorted Array
    @author oneshan
    @version 1.0 2/11/2017
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        idx = 0
        for i in range(1, len(nums)):
            if nums[idx] == nums[i]:
                continue
            else:
                idx += 1
                nums[idx] = nums[i]
        return idx + 1
