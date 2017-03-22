"""
    539 - Minimum Time Difference
    @author oneshan
    @version 1.0 3/21/2017
"""


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        time = [int(timePoint[:2]) * 60 + int(timePoint[3:]) for timePoint in timePoints]
        time.sort()
        time.append(time[0] + 1440)

        minMin = 1440
        for i in range(len(time) - 1):
            minMin = min(minMin, time[i + 1] - time[i])

        return minMin
