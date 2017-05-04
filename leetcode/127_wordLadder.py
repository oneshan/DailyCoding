from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        queue = deque([(beginWord, 1)])
        wordSet = set(wordList)

        while queue:
            currWord, ans = queue.popleft()
            if currWord == endWord:
                return ans

            for i in range(len(currWord)):
                part1 = currWord[:i]
                part2 = currWord[i + 1:]
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if currWord[i] != c:
                        nextWord = part1 + c + part2
                        if nextWord in wordSet:
                            queue.append((nextWord, ans + 1))
                            wordSet.remove(nextWord)
        return 0
