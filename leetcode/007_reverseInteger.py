"""
    007 - Reverse Integer
    @author oneshan
    @version 1.0 2/28/2017
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x >= 0 else -1
        x *= sign

        ans = 0
        while x:
            ans *= 10
            ans += x % 10
            x /= 10

        if ans >= 1 << 31:
            return 0

        return ans * sign
