"""
    567 - Permutation in String
    @author oneshan
    @version 1.0 5/20/2017
"""


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        arr = [0] * 26
        for ch in s1:
            arr[ord(ch) - ord('a')] += 1

        window = [0] * 26
        for idx, ch in enumerate(s2):
            window[ord(ch) - ord('a')] += 1
            if idx >= len(s1):
                window[ord(s2[idx - len(s1)]) - ord('a')] -= 1
            if window == arr:
                return True
        return False
