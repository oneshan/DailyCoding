"""
    217 - Contains Duplicate
    @author oneshan
    @version 1.0 2/5/2017
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = {}
        for n in nums:
            if n in seen:
                return True
            seen[n] = None

        return False
