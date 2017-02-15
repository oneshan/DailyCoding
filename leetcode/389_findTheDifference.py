"""
    389 - Find the Difference
    @author oneshan
    @version 1.0 2/14/2017
"""


class Solution(object):
    """ Using bit manipulation """
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans = 0
        for ch in s + t:
            ans ^= ord(ch)
        return chr(ans)


class Solution_2(object):
    """ Using hash table """
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hash = {}
        for ch in s:
            hash.setdefault(ch, 0)
            hash[ch] += 1
        for ch in t:
            if hash.get(ch, 0) == 0:
                return ch
            hash[ch] -= 1
