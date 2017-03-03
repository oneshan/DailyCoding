"""
    374 - Guess Number Higher or Lower
    @author oneshan
    @version 1.0 3/2/2017
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) / 2
            val = guess(mid)
            if val == 1:
                left = mid + 1
            elif val == -1:
                right = mid - 1
            else:
                return mid
