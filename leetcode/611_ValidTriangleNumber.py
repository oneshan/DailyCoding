"""
    611 - Valid Triangle Number
    @author oneshan
    @version 1.0 6/22/2017
"""


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0

        nums.sort()
        for k in range(len(nums) - 1, -1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] <= nums[k]:
                    i += 1
                else:
                    ans += j - i
                    j -= 1
        return ans
