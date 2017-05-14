"""
    547 - Friend Circles
    @author oneshan
    @version 1.0 5/14/2017
"""


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        size = len(M)
        parent = list(range(size))
        ans = size

        def find_parent(parent, i):
            if parent[i] != i:
                return find_parent(parent, parent[i])
            return parent[i]

        for i in range(size):
            for j in range(i):
                if M[i][j]:
                    root_i = find_parent(parent, i)
                    root_j = find_parent(parent, j)
                    if root_i != root_j:
                        parent[root_i] = root_j
                        ans -= 1

        return ans


class Solution_2(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        size = len(M)
        ans = 0

        for i in range(size):
            if not M[i][i]:
                continue
            stack = [i]
            while stack:
                curr = stack.pop()
                if not M[curr][curr]:
                    continue
                M[curr][curr] = 0
                for j in range(size):
                    if M[curr][j] and M[j][j]:
                        stack.append(j)
            ans += 1

        return ans
