"""
    064 - Minimum Path Sum
    @author oneshan
    @version 1.0 5/28/2017
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        M = len(grid)
        N = len(grid[0])

        for i in range(1, M):
            grid[i][0] += grid[i - 1][0]
        for j in range(1, N):
            grid[0][j] += grid[0][j - 1]
        for i in range(1, M):
            for j in range(1, N):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]
