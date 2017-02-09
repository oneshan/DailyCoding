"""
    136 - Single Number
    Time: O(n), Space: O(1) -- use XOR

    @author oneshan
    @version 1.0 2/8/2017
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        for i in range(1, len(nums)):
            result = result ^ nums[i]
        return result
