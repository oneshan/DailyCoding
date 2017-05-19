"""
    557 - Reverse Words in a String III
    @author oneshan
    @version 1.0 5/19/2017
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(tmp[::-1] for tmp in s.split())
