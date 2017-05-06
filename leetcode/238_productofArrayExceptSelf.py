"""
    238 - Product of Array Except Self
    @author oneshan
    @version 1.0 5/5/2017
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1 for _ in range(n)]

        p1, p2 = 1, 1
        for i in range(n):
            ans[i] *= p1
            ans[-1 - i] *= p2
            p1 *= nums[i]
            p2 *= nums[-1 - i]
        return ans
