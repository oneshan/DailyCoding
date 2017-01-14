"""
    242. Valid Anagram
    @author oneshan
    @version 1.0 1/13/2017
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        table = [0 for _ in range(26)]
        for c in s:
            table[ord(c) - 97] += 1

        for c in t:
            table[ord(c) - 97] -= 1
            if table[ord(c) - 97] < 0:
                return False
        return True
