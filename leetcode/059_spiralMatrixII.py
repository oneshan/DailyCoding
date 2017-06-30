"""
    059 - Spiral Matrix II
    @author oneshan
    @version 1.0 6/28/2017
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        count = 1
        row_s, row_e = 0, n - 1
        col_s, col_e = 0, n - 1

        while row_s <= row_e and col_s <= col_e:
            for j in range(col_s, col_e + 1):
                matrix[row_s][j] = count
                count += 1
            row_s += 1

            for i in range(row_s, row_e + 1):
                matrix[i][col_e] = count
                count += 1
            col_e -= 1

            if row_s <= row_e:
                for j in range(col_e, col_s - 1, -1):
                    matrix[row_e][j] = count
                    count += 1
                row_e -= 1

            if col_s <= col_e:
                for i in range(row_e, row_s - 1, -1):
                    matrix[i][col_s] = count
                    count += 1
                col_s += 1

        return matrix
