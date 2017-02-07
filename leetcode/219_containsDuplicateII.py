"""
    219 - Contains Duplicate II
    @author oneshan
    @version 1.0 2/5/2017
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        for idx, n in enumerate(nums):
            if n in seen and idx - seen[n] <= k:
                return True
            seen[n] = idx
        return False
