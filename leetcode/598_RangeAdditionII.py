"""
    598 - Range Addition II
    @author oneshan
    @version 1.0 5/31/2017
"""


class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        min_x, min_y = m, n
        for x, y in ops:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
        return min_x * min_y
