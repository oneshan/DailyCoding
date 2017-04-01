"""
    080 - Remove Duplicates from Sorted Array II
    @author oneshan
    @version 1.0 3/31/2017
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return n

        j = 1
        for i in range(2, n):
            if nums[j - 1] < nums[i]:
                j += 1
                nums[j] = nums[i]
        return j + 1


class Solution_2(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for n in nums:
            if j < 2 or n > nums[j - 2]:
                nums[j] = n
                j += 1
        return j
