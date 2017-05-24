"""
    594 - Longest Harmonious Subsequence
    @author oneshan
    @version 1.0 5/24/2017
"""


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        ans = 0
        for num in count:
            if num + 1 in count:
                ans = max(ans, count[num] + count[num + 1])

        return ans
