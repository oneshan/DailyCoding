"""
    485 - Max Consecutive Ones
    @author oneshan
    @version 1.0 2/10/2017
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        count = 0
        for num in nums:
            if num == 0:
                ans = max(ans, count)
                count = 0
            else:
                count += 1
        ans = max(ans, count)
        return ans


class Solution_2(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = -1
        ans = 0

        nums.append(0)
        for idx, num in enumerate(nums):
            if num == 0:
                ans = max(ans, idx - prev - 1)
                prev = idx
        return ans
