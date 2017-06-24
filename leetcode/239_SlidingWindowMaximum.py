"""
    239 - Sliding Window Maximum 
    @author oneshan
    @version 1.0 6/23/2017
"""


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue = []
        ans = []
        for idx, num in enumerate(nums):
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(idx)
            if queue[0] == idx - k:
                queue.pop(0)
            if idx >= k - 1:
                ans.append(nums[queue[0]])
        return ans
