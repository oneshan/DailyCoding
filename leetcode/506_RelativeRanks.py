"""
    506 - Relative Ranks
    @author oneshan
    @version 1.0 4/3/2017
"""


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        table = {}
        for rank, num in enumerate(sorted(nums, reverse=True)):
            table[num] = rank

        ans = [None] * len(nums)
        for i in range(len(nums)):
            rank = table[nums[i]]
            if rank < 3:
                ans[i] = ("Gold Medal", "Silver Medal", "Bronze Medal")[rank]
            else:
                ans[i] = str(rank + 1)
        return ans
