"""
    474 - Ones and Zeroes
    @author oneshan
    @version 1.0 4/1/2017
"""


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zero, one = s.count("0"), s.count("1")
            for i in range(m, zero - 1, -1):
                for j in range(n, one - 1, -1):
                    if i >= zero and j >= one:
                        dp[i][j] = max(dp[i][j], 1 + dp[i - zero][j - one])
        return dp[m][n]
