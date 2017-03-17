"""
    436 - Find Right Interval
    @author oneshan
    @version 1.0 3/16/2017
"""


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        arr = sorted([(interval.start, idx) for idx, interval in enumerate(intervals)])
        ans = []
        for interval in intervals:
            idx = self.binary_search(arr, interval.end)
            ans.append(idx)
        return ans

    def binary_search(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if arr[mid][0] == target:
                return arr[mid][1]
            elif arr[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        return arr[left][1] if left < len(arr) else -1
