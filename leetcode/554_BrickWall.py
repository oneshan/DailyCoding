"""
    554 - Brick Wall
    @author oneshan
    @version 1.0 6/1/2017
"""


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        table = {}
        for row in wall:
            num = 0
            for i in range(len(row) - 1):
                num += row[i]
                table[num] = table.get(num, 0) + 1
        return len(wall) - max(table.values() + [0])
