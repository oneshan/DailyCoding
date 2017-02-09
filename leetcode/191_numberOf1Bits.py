"""
    191 - Number of 1 Bits
    @author oneshan
    @version 1.0 2/9/2017
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(32):
            count += n & 1
            n >>= 1
        return count
