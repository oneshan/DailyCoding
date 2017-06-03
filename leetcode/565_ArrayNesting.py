"""
    565 - Array Nesting
    @author oneshan
    @version 1.0 6/3/2017
"""


class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unseen = [1 for _ in range(len(nums))]
        ans = 0
        for i in range(len(nums)):
            count, curr = 0, nums[i]
            while unseen[curr]:
                unseen[curr] = 0
                count, curr = count + 1, nums[curr]
            ans = max(ans, count)
        return ans
