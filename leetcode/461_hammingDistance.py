"""
    461 - Hamming Distance Add to List
    @author oneshan
    @version 1.0 2/22/2017
"""


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        num = x ^ y
        count = 0

        while num:
            count += num & 1
            num >>= 1
        return count
