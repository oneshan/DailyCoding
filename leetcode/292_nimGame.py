"""
    292 - Nim Game
    @author oneshan
    @version 1.0 2/23/2017
"""


class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n % 4 != 0)
