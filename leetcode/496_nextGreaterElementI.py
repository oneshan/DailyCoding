"""
    496 - Next Greater Element I
    @author oneshan
    @version 1.0 2/6/2017
"""


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        nextGreater = {}

        for num in nums:
            while (stack and stack[-1] < num):
                popped = stack.pop()
                nextGreater[popped] = num
            stack.append(num)

        ans = [nextGreater.get(num, -1) for num in findNums]
        return ans
