"""
    438 - Find All Anagrams in a String
    @author oneshan
    @version 1.0 5/19/2017
"""


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        arr = [0] * 256
        for ch in p:
            arr[ord(ch)] += 1

        ans = []
        window = [0] * 256
        for idx, ch in enumerate(s):
            window[ord(ch)] += 1
            if idx >= len(p):
                window[ord(s[idx - len(p)])] -= 1
            if window == arr:
                ans.append(idx - len(p) + 1)
        return ans
