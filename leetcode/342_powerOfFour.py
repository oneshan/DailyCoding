"""
    342 - Power of Four
    @author oneshan
    @version 1.0 2/22/2017
             1.1 5/09/2017
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


class Solution_2(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num & (num - 1) == 0 and num & 0x55555555 > 0
