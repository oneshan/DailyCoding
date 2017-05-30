"""
    477 - Total Hamming Distance
    @author oneshan
    @version 1.0 5/30/2017
"""


class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, mask = 0, 1
        for i in range(32):
            ones, zeros = 0, 0
            for num in nums:
                if num & mask:
                    ones += 1
                else:
                    zeros += 1
            ans += ones * zeros
            mask <<= 1
        return ans
