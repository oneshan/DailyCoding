"""
    264 - Ugly Number II
    @author oneshan
    @version 1.0 2/5/2017
"""


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [0, 1]
        n2, n3, n5 = 1, 1, 1
        for i in range(1, n):
            if ans[n2] * 2 <= ans[i]:
                n2 += 1
            if ans[n3] * 3 <= ans[i]:
                n3 += 1
            if ans[n5] * 5 <= ans[i]:
                n5 += 1
            ans.append(min(ans[n2] * 2, min(ans[n3] * 3, ans[n5] * 5)))

        return ans[n]
