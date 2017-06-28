"""
    039 - Combination Sum
    @author oneshan
    @version 1.0 6/28/2017
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()

        def dfs(remains, combo, index):
            if remains == 0:
                ans.append(combo)
                return
            for idx in range(index, len(candidates)):
                if remains - candidates[idx] < 0:
                    break
                dfs(remains - candidates[idx], combo + [candidates[idx]], idx)

        dfs(target, [], 0)
        return ans
