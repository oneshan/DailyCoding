"""
    168 - Excel Sheet Column Title
    @author oneshan
    @version 1.0 2/28/2017
"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""

        mapping = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = ""

        while n:
            n -= 1
            ans = mapping[n % 26] + ans
            n /= 26

        return ans
