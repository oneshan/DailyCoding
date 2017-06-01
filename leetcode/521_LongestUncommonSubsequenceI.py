"""
    521 - Longest Uncommon Subsequence I
    @author oneshan
    @version 1.0 5/31/2017
"""


class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        return max(len(a), len(b))
