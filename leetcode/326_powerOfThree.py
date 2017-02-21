"""
    326 - Power of Three
    @author oneshan
    @version 1.0 2/20/2017
"""


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return (pow(3, 30) % n == 0)
