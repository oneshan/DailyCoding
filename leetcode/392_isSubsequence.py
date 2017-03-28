"""
    392 - Is Subsequence
    @author oneshan
    @version 1.0 3/27/2017
"""


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, n = 0, len(s)
        if i == n:
            return True

        for ch in t:
            if ch == s[i]:
                i += 1
                if i == n:
                    return True
        return False
