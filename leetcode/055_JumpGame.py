"""
    055 - Jump Game
    @author oneshan
    @version 1.0 3/26/2017
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_loc = 0
        for i in range(len(nums)):
            if max_loc >= len(nums):
                return True
            if max_loc < i:
                return False
            max_loc = max(i + nums[i], max_loc)
        return True
