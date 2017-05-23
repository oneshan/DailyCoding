"""
    334 - Increasing Triplet Subsequence
    @author oneshan
    @version 1.0 5/23/2017
"""


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
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
                if len(self.lis) == 3:
                    return True
            else:
                self.lis[pos] = num

        return False
