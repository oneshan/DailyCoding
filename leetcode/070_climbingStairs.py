"""
    070 - Climbing Stairs
    @author oneshan
    @version 1.0 3/6/2017
    @version 1.1 5/2/2017
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


class Solution_2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        p2, p1 = 0, 1
        for i in range(n):
            p2, p1 = p1, p1 + p2
        return p1
