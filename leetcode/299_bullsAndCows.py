"""
    299 - Bulls and Cows
    @author oneshan
    @version 1.0 5/27/2017
"""


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        num = {}
        for ch in "0123456789":
            num[ch] = 0

        A, B = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                if num[secret[i]] < 0:
                    B += 1
                num[secret[i]] += 1
                if num[guess[i]] > 0:
                    B += 1
                num[guess[i]] -= 1

        return "{0}A{1}B".format(A, B)
