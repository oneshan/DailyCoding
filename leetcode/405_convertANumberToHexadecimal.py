"""
    405 - Convert a Number to Hexadecimal
    @author oneshan
    @version 1.0 5/9/2017
"""


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        strHex = "0123456789abcdef"
        ans = ""
        if num < 0:
            num += 1 << 32
        while num:
            ans = strHex[num & 15] + ans
            num >>= 4
        return ans
