"""
    001 - Two Sum
    @author oneshan
    @version 1.0 1/9/2017
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for idx, num in enumerate(nums):
            x = target - num
            if x in dict:
                return [dict[x], idx]
            dict[num] = idx
