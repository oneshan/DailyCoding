"""
    137 - Single Number II

    @author oneshan
    @version 1.0 2/8/2017
    @version 2.0 3/11/2017
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = {}
        for num in nums:
            result.setdefault(num, 0)
            result[num] += 1

        for num in result:
            if result[num] == 1:
                return num


class Solution_2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0

        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1
            count %= 3

            # deal with the negative situation
            if i == 31 and count:
                ans -= 1 << 31
            else:
                ans |= count << i

        return ans
