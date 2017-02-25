"""
    455 - Assign Cookies
    @author oneshan
    @version 1.0 2/25/2017
"""


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        m, n = 0, 0
        ans = 0
        while m < len(g) and n < len(s):
            if g[m] <= s[n]:
                m += 1
                ans += 1
            n += 1
        return ans
