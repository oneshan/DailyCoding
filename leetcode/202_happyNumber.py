"""
    202 - Happy Number
    @author oneshan
    @version 1.0 2/5/2017
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = {n: None}
        while n != 1:
            n = self.getSum(n)
            if n in seen:
                return False
            seen[n] = None
        return True

    def getSum(self, n):
        sum = 0
        while n:
            digit = n % 10
            sum += digit * digit
            n /= 10
        return sum
