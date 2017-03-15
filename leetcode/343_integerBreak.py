"""
    343 - Integer Break
    @author oneshan
    @version 1.0 3/14/2017
"""


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 0, 1, 2, 4, 6, 9] + [0] * (n - 6)
        for i in range(7, n + 1):
            dp[i] = max(dp[i - 2] * 2, dp[i - 3] * 3)
        return dp[n]
