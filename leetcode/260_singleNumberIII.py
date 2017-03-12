"""
    260 - Single Number III
    @author oneshan
    @version 1.0 3/11/2017
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor = xor ^ num

        mask = 1  
        x, y = 0, 0
        while(xor & mask == 0):
            mask = mask << 1

        for num in nums:
            if num & mask:
                x ^= num
            else:
                y ^= num

        return [x, y]
