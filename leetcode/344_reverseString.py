"""
    344. Reverse String
    @author oneshan
    @version 1.0 1/13/2017
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return "".join([s[len(s)-1-i] for i in range(len(s))])
        # return "".join([i for i in reversed(s)])
        return s[::-1]
