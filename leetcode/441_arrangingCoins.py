"""
    441 - Arranging Coins
    @author oneshan
    @version 1.0 2/15/2017
"""


class Solution(object):
    """ Brute Force: O(sqrt(n)) """
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 0
        while n > k:
            k += 1
            n -= k

        return k


class Solution_2(object):
    """ Binary Search: O(log n) """
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        left, right, ans = 1, n, n
        while left <= right:
            mid = (left + right + 1) / 2
            total = mid * (mid + 1) / 2
            if total <= n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
