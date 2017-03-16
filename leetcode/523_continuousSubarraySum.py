"""
    523 - Continuous Subarray Sum
    @author oneshan
    @version 1.0 3/15/2017
"""


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)

        if n < 2:
            return False

        if k == 0:
            for i in range(1, n):
                if nums[i - 1] == nums[i] == 0:
                    return True
                return False

        sum_list = [0]
        for num in nums:
            sum_list.append((sum_list[-1] + num) % k)

        table = {}
        for i in range(n + 1):
            key = sum_list[i]
            if key not in table:
                table[key] = i
            elif i - table[key] >= 2:
                return True
        return False
