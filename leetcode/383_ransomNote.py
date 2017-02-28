"""
    383 - Ransom Note
    @author oneshan
    @version 1.0 2/27/2017
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        table = {}
        for ch in magazine:
            table[ch] = 1 + table.get(ch, 0)
        for ch in ransomNote:
            if ch not in table:
                return False
            elif table[ch] == 0:
                return False
            table[ch] -= 1
        return True
