"""
    476 - Number Complement
    @author oneshan
    @version 1.0 2/22/2017
"""


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        power2 = 1
        while power2 < num:
            power2 <<= 1

        if power2 == num:
            return power2 - 1
        return num ^ (power2 - 1)
