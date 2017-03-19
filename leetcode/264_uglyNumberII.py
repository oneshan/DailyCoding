"""
    264 - Ugly Number II
    @author oneshan
    @version 1.0 2/5/2017
    @version 2.0 3/18/2017
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


class Solution_2(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [0] * n
        ugly[0] = 1

        p2, p3, p5 = 0, 0, 0
        n2, n3, n5 = 2, 3, 5

        for i in range(1, n):
            ugly[i] = min(n2, n3, n5)
            if n2 == ugly[i]:
                p2 += 1
                n2 = ugly[p2] * 2

            if n3 == ugly[i]:
                p3 += 1
                n3 = ugly[p3] * 3

            if n5 == ugly[i]:
                p5 += 1
                n5 = ugly[p5] * 5

        return ugly[-1]
