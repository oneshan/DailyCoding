"""
    345 - Reverse Vowels of a String
    @author oneshan
    @version 1.0 2/21/2017
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        p1, p2 = 0, len(s) - 1
        temp = list(s)

        while p1 < p2:
            while s[p1] not in "aeiouAEIOU" and p1 < p2:
                p1 += 1
            while s[p2] not in "aeiouAEIOU" and p1 < p2:
                p2 -= 1

            if p1 != p2:
                temp[p1], temp[p2] = temp[p2], temp[p1]

            p1 += 1
            p2 -= 1

        return "".join(temp)
