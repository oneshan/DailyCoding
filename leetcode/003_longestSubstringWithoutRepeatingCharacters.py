"""
    003 - Longest Substring Without Repeating Characters
    @author oneshan
    @version 1.0 2/5/2017
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        ans = 0
        left = 0
        pos = dict()
        for i in range(len(s)):
            if s[i] in pos and pos[s[i]] >= left:
                left = pos[s[i]] + 1
            pos[s[i]] = i
            ans = max(ans, i - left + 1)

        return ans
