"""
    520 - Detect Capital
    @author oneshan
    @version 1.0 2/22/2017
"""


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 1:
            return True

        preUpper = (word[1] < 'a')
        for idx in range(2, len(word)):
            if word[idx] < 'a':
                if not preUpper:
                    return False
                preUpper = True
            else:
                if preUpper:
                    return False
                preUpper = False

        # word[0] is lower and others are upper
        if word[0] >= 'a' and preUpper:
            return False

        return True
