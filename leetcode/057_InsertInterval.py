"""
    057 - Insert Interval
    @author oneshan
    @version 1.0 6/28/2017
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals = (
            [i for i in intervals if i.start <= newInterval.start] +
            [newInterval] +
            [i for i in intervals if i.start > newInterval.start]
        )

        ans = [Interval(-1, -1)]
        for i in intervals:
            if i.start > ans[-1].end:
                ans += i,
            else:
                ans[-1].end = max(ans[-1].end, i.end)
        return ans[1:]


class Solution_2(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        left, right = [], []
        s, e = newInterval.start, newInterval.end
        for i in intervals:
            if i.end < s:
                left += i,
            elif i.start > e:
                right += i,
            else:
                s = min(s, i.start)
                e = max(e, i.end)
        return left + [Interval(s, e)] + right
