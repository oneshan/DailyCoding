"""
    553 - Optimal Division
    @author oneshan
    @version 1.0 6/2/2017
"""


class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str, nums)
        if len(nums) < 3:
            return "/".join(nums)
        return "{}/({})".format(nums[0], "/".join(nums[1:]))
