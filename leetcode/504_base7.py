"""
    504 - Base 7
    @author oneshan
    @version 1.0 2/26/2017
"""


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        sign, num = (num > 0), abs(num)
        ans = ""
        while num:
            ans = str(num % 7) + ans
            num /= 7

        return ("-", "")[sign] + ans
