"""
    119 - Pascal's Triangle II
    @author oneshan
    @version 1.0 2/18/2017
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        inner = [1]
        for i in range(rowIndex):
            inner = [1] + [inner[j] + inner[j - 1] for j in range(1, i + 1)] + [1]
        return inner
