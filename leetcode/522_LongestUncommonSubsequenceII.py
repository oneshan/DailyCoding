"""
    521 - Longest Uncommon Subsequence I
    @author oneshan
    @version 1.0 5/31/2017
"""


class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        def check(s1, s2):
            i = 0
            for ch in s2:
                if ch == s1[i]:
                    i += 1
                if i == len(s1):
                    return True
            return False

        table = {}
        for str in strs:
            table[str] = table.get(str, 0) + 1
        once = sorted([key for key in table if table[key] == 1], key=len)[::-1]

        for str1 in once:
            for str2 in table:
                if str1 == str2:
                    continue
                if check(str1, str2):
                    break
            else:
                return len(str1)
        return -1
