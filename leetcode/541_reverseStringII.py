"""
    541 - Reverse String II
    @author oneshan
    @version 1.0 3/19/2017
"""


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        ans = ""
        for i in range(0, n, 2 * k):
            ans += s[i: i + k][::-1] + s[i + k:i + 2 * k]
        return ans
