"""
    560 - Subarray Sum Equals K
    @author oneshan
    @version 1.0 6/26/2017
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        table = {0: 1}
        ans, preSum = 0, 0
        for num in nums:
            preSum += num
            ans += table.get(preSum - k, 0)
            table[preSum] = table.get(preSum, 0) + 1
        return ans
