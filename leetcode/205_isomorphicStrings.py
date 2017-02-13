"""
    205 - Isomorphic Strings
    @author oneshan
    @version 1.0 2/12/2017
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_t, t_s = {}, {}
        for idx in range(len(s)):
            if s[idx] not in s_t:
                s_t[s[idx]] = t[idx]
            elif s_t[s[idx]] != t[idx]:
                return False

            if t[idx] not in t_s:
                t_s[t[idx]] = s[idx]
            elif t_s[t[idx]] != s[idx]:
                return False

        return True
