"""
    300 - Longest Increasing Subsequence
    @author oneshan
    @version 1.0 5/23/2017
"""


class Solution(object):
    """ Using DP, time complexity: O(n^2) """
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dp = [1] * len(nums)
        for idx, num in enumerate(nums):
            preMax = 0
            for j in range(idx):
                if num > nums[j]:
                    preMax = max(preMax, dp[j])
            dp[idx] = preMax + 1

        return max(dp)


class Solution_2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.lis = []

        def search(val):
            left, right = 0, len(self.lis) - 1
            while left <= right:
                mid = left + (right - left) / 2
                if self.lis[mid] == val:
                    return mid
                elif self.lis[mid] > val:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        for num in nums:
            pos = search(num)
            if pos == len(self.lis):
                self.lis.append(num)
            else:
                self.lis[pos] = num

        return len(self.lis)
