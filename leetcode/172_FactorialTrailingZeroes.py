"""
    172 - Factorial Trailing Zeroes
    @author oneshan
    @version 1.0 3/2/2017
"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n:
            n /= 5
            ans += n
        return ans
