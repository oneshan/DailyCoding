"""
    290 - Word Pattern
    @author oneshan
    @version 1.0 2/13/2017
"""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        str_list = str.split()
        if len(str_list) != len(pattern):
            return False

        p_s, s_p = {}, {}
        for idx in range(len(pattern)):
            if p_s.get(pattern[idx], None) != s_p.get(str_list[idx], None):
                return False
            p_s[pattern[idx]] = idx
            s_p[str_list[idx]] = idx
        return True
