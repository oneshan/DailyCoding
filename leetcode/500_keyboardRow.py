"""
    500 - Keyboard Row
    @author oneshan
    @version 1.0 5/21/2017
"""


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        ans = []

        for word in words:
            for row in keyboard:
                if word[0].lower() in row:
                    break
            for char in word.lower():
                if char not in row:
                    break
            else:
                ans.append(word)
        return ans
