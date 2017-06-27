"""
    041 - First Missing Positive
    @author oneshan
    @version 1.0 6/27/2017
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.append(0)

        for i in range(len(nums)):
            while True:
                if nums[i] <= 0 or nums[i] >= len(nums) or nums[nums[i]] == nums[i]:
                    break
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        for i in range(1, len(nums)):
            if nums[i] != i:
                return i

        return len(nums)
