"""
    434 - Number of Segments in a String
    @author oneshan
    @version 1.0 2/12/2017
"""


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        preIsChar = False
        for ch in s:
            if ch == " " and preIsChar:
                count += 1
            preIsChar = (ch != " ")
        if preIsChar:
            count += 1
        return count
