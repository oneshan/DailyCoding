"""
    120 - Triangle
    @author oneshan
    @version 1.0 3/30/2017
"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return None

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] = min(triangle[i + 1][j], triangle[i + 1][j + 1]) + triangle[i][j]
        return triangle[0][0]
