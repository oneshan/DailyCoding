class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # ans = ((m-1)+(n-1))! / (m-1)!(n-1)!
        ans = 1
        i, j = max(m, n), 1
        while i < m + n - 1:
            ans *= i
            ans /= j
            i += 1
            j += 1
        return ans


class Solution_2(object):
    """ DP """
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * n] * m
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
