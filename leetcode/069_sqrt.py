"""
    069 - Sqrt(x)
    @author oneshan
    @version 1.0 3/6/2017
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left, right = 1, x
        while left <= right:
            mid = left + (right - left) / 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid
        return right
