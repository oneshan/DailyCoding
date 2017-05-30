"""
    318 - Maximum Product of Word Lengths
    @author oneshan
    @version 1.0 5/30/2017
"""


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        table = [0 for _ in range(n)]
        for idx, word in enumerate(words):
            for ch in word:
                table[idx] |= 1 << (ord(ch) - 97)

        ans = 0
        for i in range(1, n):
            for j in range(i):
                if table[i] & table[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans
