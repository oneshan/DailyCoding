"""
    028 - Implement strStr()
    @author oneshan
    @version 1.0 3/24/2017
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] != needle[0]:
                continue
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1
