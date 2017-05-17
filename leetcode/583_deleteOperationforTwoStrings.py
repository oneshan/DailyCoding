"""
    583 - Delete Operation for Two Strings
    @author oneshan
    @version 1.0 5/17/2017
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1, len2 = len(word1), len(word2)
        dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        for i in range(len1):
            for j in range(len2):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return len1 + len2 - (dp[len1][len2] << 1)
