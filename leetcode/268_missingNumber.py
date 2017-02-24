"""
    268 - Missing Number
    @author oneshan
    @version 1.0 2/22/2017
"""


class Solution(object):
    """ SUM version """
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = (len(nums) + 1) * len(nums) / 2
        for num in nums:
            total -= num
        return total


class Solution_2(object):
    """ XOR version """
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = len(nums)
        for i in range(len(nums)):
            ans ^= i
            ans ^= nums[i]
        return ans
