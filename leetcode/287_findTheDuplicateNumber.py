"""
    287 - Find the Duplicate Number
    @author oneshan
    @version 1.0 5/16/2017
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            count = sum(1 for num in nums if num <= mid)
            if count > mid:
                right = mid - 1
            else:
                left = mid + 1
        return left


class Solution_2(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast, slow = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow
