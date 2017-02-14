"""
    118 - Pascal's Triangle
    @author oneshan
    @version 1.0 2/13/2017
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        ans = [[1]]
        inner = []
        for i in range(numRows - 1):
            inner = [1] + [inner[j] + inner[j - 1] for j in range(1, i + 1)] + [1]
            ans.append(inner)
        return ans
