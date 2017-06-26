"""
    016 - 3Sum Closest
    @author oneshan
    @version 1.0 6/25/2017
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = 0
        min_diff = float("inf")
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                diff = abs(total - target)
                if diff < min_diff:
                    min_diff = diff
                    ans = total
                if total < target:
                    j += 1
                else:
                    k -= 1
        return ans
