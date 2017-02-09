"""
    367 - Valid Perfect Square
    @author oneshan
    @version 1.0 2/8/2017
"""


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 1
        right = num
        while left <= right:
            mid = (left + right) / 2
            if mid * mid < num:
                left = mid + 1
            elif mid * mid > num:
                right = mid - 1
            else:
                return True
        return False
