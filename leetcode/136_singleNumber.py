"""
    136 - Single Number

    @author oneshan
    @version 1.0 2/8/2017
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = None
            else:
                seen.pop(num)
        return seen.keys()[0]
