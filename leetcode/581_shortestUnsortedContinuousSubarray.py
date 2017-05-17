"""
    581 - Shortest Unsorted Continuous Subarray
    @author oneshan
    @version 1.0 5/17/2017
"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        p2, maxA = 0, nums[0]
        for i in range(n):
            if maxA > nums[i]:
                p2 = i
            else:
                maxA = nums[i]

        p1, minA = 0, nums[-1]
        for i in range(n - 1, -1, -1):
            if minA < nums[i]:
                p1 = i
            else:
                minA = nums[i]

        if p1 + p2 == 0:
            return 0

        return p2 - p1 + 1
