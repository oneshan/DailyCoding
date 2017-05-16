"""
    200 - Number of Islands
    @author oneshan
    @version 1.0 5/14/2017
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        ans = 0
        size_x, size_y = len(grid), len(grid[0])
        for i in range(size_x):
            for j in range(size_y):
                if grid[i][j] == '0':
                    continue
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    grid[x][y] = '0'
                    if x + 1 < size_x and grid[x + 1][y] == '1':
                        stack.append((x + 1, y))
                    if y + 1 < size_y and grid[x][y + 1] == '1':
                        stack.append((x, y + 1))
                    if x > 0 and grid[x - 1][y] == '1':
                        stack.append((x - 1, y))
                    if y > 0 and grid[x][y - 1] == '1':
                        stack.append((x, y - 1))
                ans += 1
        return ans
