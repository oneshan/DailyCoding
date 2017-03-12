"""
    169 - Majority Element
    @author oneshan
    @version 1.0 3/11/2017
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, major = 0, None

        for num in nums:
            if count == 0:
                count, major = 1, num
            elif major == num:
                count += 1
            else:
                count -= 1

        return major
