"""
    258 - Add Digits
    @author oneshan
    @version 1.0 2/5/2017
"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return (num - 1) % 9 + 1
