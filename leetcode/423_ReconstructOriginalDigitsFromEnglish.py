"""
    423 - Reconstruct Original Digits from English
    @author oneshan
    @version 1.0 3/22/2017
"""


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        table = {}
        ans = {}
        pair = ((0, "z", "zero"), (2, "w", "two"), (4, "u", "four"), (6, "x", "six"),
                (8, "g", "eight"), (1, "o", "one"), (3, "r", "three"), (5, "f", "five"),
                (7, "s", "seven"), (9, "i", "nine"))

        for ch in s:
            table[ch] = table.get(ch, 0) + 1

        for i, key, string in pair:
            ans[i] = table.get(key, 0)
            if ans[i]:
                for ch in string:
                    table[ch] -= ans[i]

        ans_str = "".join([str(i) * ans[i] for i in range(10)])
        return ans_str
