"""
    338 - Counting Bits
    @author oneshan
    @version 1.0 2/9/2017
"""


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0 for _ in range(num + 1)]
        i = 1
        while i <= num:
            ans[i] = 1
            i <<= 1

        base = 2
        for i in range(1, num + 1):
            if ans[i]:
                base = i
            else:
                ans[i] = ans[i - base] + 1

        return ans


class Solution_2(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0 for _ in range(num + 1)]
        for i in range(num + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
