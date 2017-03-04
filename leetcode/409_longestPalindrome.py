"""
    409 - Longest Palindrome
    @author oneshan
    @version 1.0 3/4/2017
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {}
        ans = 0
        for ch in s:
            table[ch] = 1 + table.get(ch, 0)

        for ch in table:
            ans += table[ch] - (table[ch] & 1)
        if len(s) > ans:
            ans += 1

        return ans
