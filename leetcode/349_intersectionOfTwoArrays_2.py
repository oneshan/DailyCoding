"""
    349 - Intersection of Two Arrays
    version 2: sort and two pointer

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

        nums1.sort()
        nums2.sort()
        ans = []
        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                if not ans or nums1[p1] != ans[-1]:
                    ans.append(nums1[p1])
                p1 += 1
                p2 += 1
        return ans
