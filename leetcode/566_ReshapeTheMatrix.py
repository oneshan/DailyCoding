"""
    566 - Reshape the Matrix
    @author oneshan
    @version 1.0 5/19/2017
"""


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums:
            return nums

        M = len(nums)
        N = len(nums[0])
        if M * N != r * c:
            return nums

        ans = [[[0] for _ in range(c)] for _ in range(r)]

        k = 0
        for i in range(M):
            for j in range(N):
                ans[k / c][k % c] = nums[i][j]
                k += 1
        return ans
