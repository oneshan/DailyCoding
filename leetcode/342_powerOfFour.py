"""
    342 - Power of Four
    @author oneshan
    @version 1.0 2/22/2017
"""


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        while num > 1:
            if num & 3:
                return False
            num = num >> 2
        return True
