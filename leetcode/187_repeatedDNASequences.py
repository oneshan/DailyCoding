"""
    187 - Repeated DNA Sequences
    @author oneshan
    @version 1.0 3/14/2017
"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []

        table = {}
        for i in range(len(s) - 9):
            table[s[i:i + 10]] = table.get(s[i:i + 10], 0) + 1

        ans = [seq for seq in table if table[seq] > 1]
        return ans
