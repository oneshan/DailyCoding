"""
    171 - Excel Sheet Column Number
    @author oneshan
    @version 1.0 2/28/2017
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for ch in s:
            ans *= 26
            ans += ord(ch) - 64
        return ans
