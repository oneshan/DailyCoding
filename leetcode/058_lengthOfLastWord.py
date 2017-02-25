class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])


class Solution_2(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        preWord = 0
        currWord = 0
        for ch in s:
            if ch != ' ':
                currWord += 1
            elif currWord:
                preWord = currWord
                currWord = 0
        return currWord if currWord else preWord
