"""
    047 - Permutations II
    @author oneshan
    @version 1.0 6/21/2017
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []

        def dfs(perm, remains, n):
            if n == 0:
                self.ans.append(perm)
            else:
                for idx, elem in enumerate(remains):
                    if idx > 0 and remains[idx - 1] == elem:
                        continue
                    dfs(perm + [elem], remains[:idx] + remains[idx + 1:], n - 1)

        dfs([], sorted(nums), len(nums))
        return self.ans


class Solution_2(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.permute(sorted(nums))

    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]

        ans = []
        for idx, elem in enumerate(nums):
            if idx > 0 and nums[idx - 1] == elem:
                continue
            for p in self.permute(nums[:idx] + nums[idx + 1:]):
                ans.append(p + [elem])
        return ans
