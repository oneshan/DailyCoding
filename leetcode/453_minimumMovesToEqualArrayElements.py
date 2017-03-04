"""
    453 - Minimum Moves to Equal Array Elements
    @author oneshan
    @version 1.0 3/4/2017
"""


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)
