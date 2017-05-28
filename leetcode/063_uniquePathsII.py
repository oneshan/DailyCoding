"""
    063 - Unique Paths II
    @author oneshan
    @version 1.0 5/28/2017
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0

        M = len(obstacleGrid)
        N = len(obstacleGrid[0])

        obstacleGrid[0][0] ^= 1
        for i in range(1, M):
            obstacleGrid[i][0] = obstacleGrid[i-1][0] & (1 ^ obstacleGrid[i][0])
        for i in range(1, N):
            obstacleGrid[0][i] = obstacleGrid[0][i-1] & (1 ^ obstacleGrid[0][i])
        for i in range(1, M):
            for j in range(1, N):
                obstacleGrid[i][j] = 0 if obstacleGrid[i][j] else obstacleGrid[i-1][j] + obstacleGrid[i][j-1]

        return obstacleGrid[-1][-1]
