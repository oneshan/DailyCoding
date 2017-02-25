"""
    088 - Merge Sorted Array
    @author oneshan
    @version 1.0 2/24/2017
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        idx = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] < nums2[n]:
                nums1[idx] = nums2[n]
                n -= 1
            else:
                nums1[idx] = nums1[m]
                m -= 1
            idx -= 1

        if n >= 0:
            nums1[:n + 1] = nums2[:n + 1]
