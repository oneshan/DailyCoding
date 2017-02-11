"""
    448 - Find All Numbers Disappeared in an Array
    @author oneshan
    @version 1.0 2/10/2017
"""


class Solution(object):
    """ Time: O(n), Space: O(n) """
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0 for _ in range(len(nums) + 1)]
        for num in nums:
            ans[num] = 1
        return [i for i in range(1, len(nums) + 1) if not ans[i]]


class Solution_2(object):
    """ Time: O(n), Space: O(1) """
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = - abs(nums[idx])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
