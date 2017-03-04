"""
    462 - Minimum Moves to Equal Array Elements II
    @author oneshan
    @version 1.0 3/4/2017
"""


class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mid = nums[len(nums) / 2]
        return sum(abs(num - mid) for num in nums)
