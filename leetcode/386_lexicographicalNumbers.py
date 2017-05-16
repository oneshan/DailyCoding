"""
    386 - Lexicographical Numbers
    @author oneshan
    @version 1.0 5/16/2017
"""


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []

        def dfs(curr):
            if curr > n:
                return
            ans.append(curr)
            t = 10 * curr
            if t <= n:
                for i in range(10):
                    dfs(t + i)

        for i in range(1, 10):
            dfs(i)
        return ans
