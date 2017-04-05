"""
    494 - Target Sum
    @author oneshan
    @version 1.0 4/4/2017
"""


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = {0: 1}
        for num in nums:
            tmp = {}
            for s, c in dp.items():
                tmp[s + num] = tmp.get(s + num, 0) + c
                tmp[s - num] = tmp.get(s - num, 0) + c
            dp = tmp
        return dp.get(S, 0)
