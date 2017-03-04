"""
    053 - Maximum Subarray
    @author oneshan
    @version 1.0 3/3/2017
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, sum = nums[0], 0
        for i in range(len(nums)):
            sum += nums[i]
            ans = max(sum, ans)
            sum = max(sum, 0)
        return ans
