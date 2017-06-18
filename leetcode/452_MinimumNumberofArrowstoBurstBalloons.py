"""
    452 - Minimum Number of Arrows to Burst Balloons
    @author oneshan
    @version 1.0 6/16/2017
"""


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key=lambda x: x[-1])
        ans, end = 0, float('-inf')
        for point in points:
            if point[0] > end:
                ans += 1
                end = point[1]
        return ans
