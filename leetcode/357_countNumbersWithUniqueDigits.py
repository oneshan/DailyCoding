"""
    357 - Count Numbers with Unique Digits
    @author oneshan
    @version 1.0 5/21/2017
"""


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        # ans = #(0~n-1 digit) + #(n digit)
        # n = 0, ans =   1
        # n = 1, ans =   1 + (9)       = 10
        # n = 2, ans =  10 + (9*9)     = 91
        # n = 3, ans =  91 + (9*9*8)   = 739
        # n = 4, ans = 739 + (9*9*8*7) = 5275

        if n == 0:
            return 1

        ans, num = 10, 9
        for i in range(1, min(n, 10)):
            num *= (10 - i)
            ans += num
        return ans
