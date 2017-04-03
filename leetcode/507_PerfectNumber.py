"""
    507 - Perfect Number
    @author oneshan
    @version 1.0 4/2/2017
"""


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False

        i, sum = 2, 1
        while i * i < num:
            if num % i == 0:
                sum += i + num / i
            i += 1
        return sum == num
