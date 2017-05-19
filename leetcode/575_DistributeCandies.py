"""
    575 - Distribute Candies
    @author oneshan
    @version 1.0 5/19/2017
"""


class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(candies) >> 1, len(set(candies)))
