"""
    231 - Power of Two
    @author oneshan
    @version 1.0 2/20/2017
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False

        count = 0
        while n:
            count += n & 1
            n >>= 1
        return (count == 1)
