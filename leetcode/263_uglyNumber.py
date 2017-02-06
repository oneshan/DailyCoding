"""
    263 - Ugly Number
    @author oneshan
    @version 1.0 2/5/2017
"""


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False

        for prime in (2, 3, 5):
            while num % prime == 0:
                num = num / prime

        if num == 1:
            return True

        return False
