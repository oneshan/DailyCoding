"""
    415 - Add Strings
    @author oneshan
    @version 1.0 3/9/2017
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = ""
        carry = 0
        for i in range(1, max(len(num1), len(num2)) + 1):
            val = carry
            if i <= len(num1):
                val += int(num1[-i])
            if i <= len(num2):
                val += int(num2[-i])
            carry = val / 10
            val = val % 10
            ans = str(val) + ans
        if carry:
            ans = str(carry) + ans
        return ans
