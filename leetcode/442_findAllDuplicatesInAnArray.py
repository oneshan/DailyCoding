"""
    442 - Find All Duplicates in an Array
    @author oneshan
    @version 1.0 2/10/2017
"""


class Solution(object):
    """ Time: O(n), Space: O(n) """
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0 for _ in range(len(nums) + 1)]
        for num in nums:
            ans[num] += 1
        return [i for i in range(1, len(nums) + 1) if ans[i] == 2]


class Solution_2(object):
    """ Time: O(n), Space: O(1) """
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
            else:
                ans.append(idx + 1)
        return ans
