"""
    076 - Minimum Window Substring
    @author oneshan
    @version 1.0 6/23/2017
"""


class Solution(object):
    def minWindow(self, s, t):

        table = {}
        for ch in t:
            table[ch] = table.get(ch, 0) + 1
        counter = len(t)

        i = begin = end = 0
        for j, ch in enumerate(s, 1):
            table[ch] = table.get(ch, 0) - 1
            if table[ch] >= 0:
                counter -= 1
            if counter == 0:
                while i < j and table[s[i]] < 0:
                    table[s[i]] += 1
                    i += 1
                if not end or j - i <= end - begin:
                    begin, end = i, j
                counter = 1
                table[s[i]] += 1
                i += 1
        return s[begin:end]
