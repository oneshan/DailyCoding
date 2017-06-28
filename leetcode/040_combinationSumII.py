"""
    040 - Two Sum
    @author oneshan
    @version 1.0 6/28/2017
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
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
                if idx > index and candidates[idx - 1] == candidates[idx]:
                    continue
                if remains - candidates[idx] < 0:
                    break
                dfs(remains - candidates[idx], combo + [candidates[idx]], idx + 1)

        dfs(target, [], 0)
        return ans
