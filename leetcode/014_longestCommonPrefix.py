"""
    014 - Longest Common Prefix
    @author oneshan
    @version 1.0 2/24/2017
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        strs.sort()
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        return strs[0]
