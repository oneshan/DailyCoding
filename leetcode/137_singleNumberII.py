"""
    137 - Single Number II

    @author oneshan
    @version 1.0 2/8/2017
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = {}
        for num in nums:
            result.setdefault(num, 0)
            result[num] += 1

        for num in result:
            if result[num] == 1:
                return num
