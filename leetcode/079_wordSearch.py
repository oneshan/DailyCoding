"""
    079 - Word Search
    @author oneshan
    @version 1.0 4/12/2017
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        M = len(board)
        N = len(board[0])
        word_len = len(word)

        def DFS(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k + 1 == word_len:
                return True

            temp = board[i][j]
            board[i][j] = None
            hasFound = ((i > 0 and DFS(i - 1, j, k + 1)) or
                        (i < M - 1 and DFS(i + 1, j, k + 1)) or
                        (j > 0 and DFS(i, j - 1, k + 1)) or
                        (j < N - 1 and DFS(i, j + 1, k + 1)))
            board[i][j] = temp
            return hasFound

        for i in range(M):
            for j in range(N):
                if DFS(i, j, 0):
                    return True
        return False
