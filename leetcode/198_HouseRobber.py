"""
    198 - House Robber
    @author oneshan
    @version 1.0 3/23/2017
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * (len(nums) + 2)
        for i in range(len(nums)):
            dp[i + 2] = max(dp[i + 1], dp[i] + nums[i])
        return dp[-1]


class Solution_2(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre, curr = 0, 0
        for num in nums:
            pre, curr = curr, max(curr, pre + num)
        return curr
