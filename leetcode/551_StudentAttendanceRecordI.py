"""
    551 - Student Attendance Record I
    @author oneshan
    @version 1.0 6/1/2017
"""


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a, l = 0, 0
        for ch in s:
            if ch == 'A':
                a += 1
            if ch == 'L':
                l += 1
            else:
                l = 0
            if a > 1 or l > 2:
                return False
        return True
