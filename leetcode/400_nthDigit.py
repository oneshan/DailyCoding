"""
    400 - Nth Digit
    @author oneshan
    @version 1.0 2/12/2017
"""


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = 1
        count = 9
        while n > base * count:
            n -= base * count
            count *= 10
            base += 1

        num = str(pow(10, base - 1) + (n - 1) / base)
        return int(num[(n - 1) % base])
