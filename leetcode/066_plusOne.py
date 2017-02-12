"""
    066 - Plus One
    @author oneshan
    @version 1.0 2/11/2017
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        digits[-1] += 1
        while (i > 0 and digits[i] > 9):
            digits[i] -= 10
            digits[i - 1] += 1
            i = i - 1

        if digits[0] > 9:
            digits[0] -= 10
            digits = [1] + digits

        return digits
