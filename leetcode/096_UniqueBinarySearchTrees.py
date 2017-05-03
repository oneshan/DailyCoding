"""
    096 - Unique Binary Search Trees
    @author oneshan
    @version 1.0 05/02/2017
"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1, 2] + [0 for _ in range(n - 2)]

        for i in range(3, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[n]
