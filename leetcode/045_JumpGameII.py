"""
    045 - Jump Game II
    @author oneshan
    @version 1.0 6/28/2017
"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        preLen, maxLen, count = 0, 0, 0
        for i in range(len(nums)):
            if i > preLen:
                preLen = maxLen
                count += 1
            maxLen = max(maxLen, i + nums[i])
        return count
