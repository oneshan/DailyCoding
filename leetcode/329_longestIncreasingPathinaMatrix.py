"""
    329 - Longest Increasing Path in a Matrix
    @author oneshan
    @version 1.0 5/16/2017
"""


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0

        M = len(matrix)
        N = len(matrix[0])

        dp = [[0 for _ in range(N)] for _ in range(M)]

        def dfs(x, y):
            if not dp[x][y]:
                dp[x][y] = 1
                if x > 0 and matrix[x][y] < matrix[x - 1][y]:
                    dp[x][y] = max(dp[x][y], dfs(x - 1, y) + 1)
                if x < M - 1 and matrix[x][y] < matrix[x + 1][y]:
                    dp[x][y] = max(dp[x][y], dfs(x + 1, y) + 1)
                if y > 0 and matrix[x][y] < matrix[x][y - 1]:
                    dp[x][y] = max(dp[x][y], dfs(x, y - 1) + 1)
                if y < N - 1 and matrix[x][y] < matrix[x][y + 1]:
                    dp[x][y] = max(dp[x][y], dfs(x, y + 1) + 1)
            return dp[x][y]

        for i in range(M):
            for j in range(N):
                dfs(i, j)

        return max(dp[i][j] for i in range(M) for j in range(N))
