"""
    054 - Spiral Matrix
    @author oneshan
    @version 1.0 2/21/2017
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        start_row, start_col = 0, 0
        end_row, end_col = len(matrix) - 1, len(matrix[0]) - 1

        ans = []

        while start_row <= end_row and start_col <= end_col:
            for i in range(start_col, end_col + 1):
                ans.append(matrix[start_row][i])
            start_row += 1

            for i in range(start_row, end_row + 1):
                ans.append(matrix[i][end_col])
            end_col -= 1

            if start_row <= end_row:
                for i in range(end_col, start_col - 1, -1):
                    ans.append(matrix[end_row][i])
                end_row -= 1

            if start_col <= end_col:
                for i in range(end_row, start_row - 1, -1):
                    ans.append(matrix[i][start_col])
                start_col += 1

        return ans
