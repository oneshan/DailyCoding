"""
    463 - Island Perimeter
    @author oneshan
    @version 1.0 4/5/2017
"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        ans -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        ans -= 2
        return ans
