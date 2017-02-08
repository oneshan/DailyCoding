"""
    349 - Intersection of Two Arrays
    @author oneshan
    @version 1.0 2/7/2017
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []

        return list(set(nums1) & set(nums2))
