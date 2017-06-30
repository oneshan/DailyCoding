"""
    056 - Merge Intervals
    @author oneshan
    @version 1.0 6/28/2017
"""


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = [Interval(-1, -1)]
        for interval in sorted(intervals, key=lambda i: i.start):
            if interval.start > ans[-1].end:
                ans += interval,
            else:
                ans[-1].end = max(ans[-1].end, interval.end)
        return ans[1:]
