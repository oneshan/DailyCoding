"""
    075
    @author oneshan
    @version 1.0 3/29/2017
"""


class Solution(object):
    """ Count Sort O(m+n)  m: #color, n: #nums """
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1
        idx = 0
        for i in range(3):
            while count[i]:
                nums[idx] = i
                idx += 1
                count[i] -= 1


class Solution_2(object):
    """ Two pointer with swap O(n) """
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p0, p2 = 0, len(nums) - 1
        i = 0
        while p0 <= i <= p2:
            if nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                p0 += 1
            elif nums[i] == 2:
                nums[p2], nums[i] = nums[i], nums[p2]
                p2 -= 1
                i -= 1
            i += 1


class Solution_3(object):
    """ Two pointer without swap O(n) """
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p0, p1 = 0, 0
        for i in range(len(nums)):
            tmp = nums[i]
            nums[i] = 2
            if tmp < 2:
                nums[p1] = 1
                p1 += 1
            if tmp == 0:
                nums[p0] = 0
                p0 += 1
