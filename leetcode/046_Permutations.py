"""
    046 - Permutations
    @author oneshan
    @version 1.0 6/21/2017
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []

        def dfs(perm, remains, n):
            if n == 0:
                self.ans.append(perm)
            for i in range(len(remains)):
                dfs(perm + [remains[i]], remains[:i] + remains[i + 1:], n - 1)

        dfs([], nums, len(nums))
        return self.ans


class Solution_2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]

        ans = []
        for idx, elem in enumerate(nums):
            for p in self.permute(nums[:idx] + nums[idx + 1:]):
                ans.append(p + [elem])
        return ans


