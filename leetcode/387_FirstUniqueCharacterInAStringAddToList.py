"""
    387 - First Unique Character in a String Add to List
    @author oneshan
    @version 1.0 2/25/2017
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        table = {}
        for idx, ch in enumerate(s):
            if ch in table:
                table[ch] = len(s)
            else:
                table[ch] = idx

        ans = len(s)
        for ch in table:
            if table[ch] < ans:
                ans = table[ch]

        if ans == len(s):
            return -1

        return ans
