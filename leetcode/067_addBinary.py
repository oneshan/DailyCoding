"""
    067 - Add Binary
    @author oneshan
    @version 1.0 2/26/2017
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        ans, digit = "", 0
        idx = 1

        while idx <= max(len(a), len(b)):
            if len(a) >= idx and a[-idx] == '1':
                digit += 1
            if len(b) >= idx and b[-idx] == '1':
                digit += 1
            ans = str(digit & 1) + ans
            digit = (digit >> 1) & 1
            idx += 1

        if digit:
            ans = "1" + ans

        return ans
