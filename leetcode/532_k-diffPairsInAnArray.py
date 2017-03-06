"""
    532 - K-diff Pairs in an Array
    @author oneshan
    @version 1.0 3/5/2017
"""


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        pair = []
        nums.sort()
        i, j = 0, 1

        while i < j < len(nums):
            if nums[j] - nums[i] < k:
                j += 1
            elif nums[j] - nums[i] > k:
                i += 1
            else:
                pair.append((nums[i], nums[j]))
                i += 1
                j += 1
            if i == j:
                j += 1
        return len(set(pair))
