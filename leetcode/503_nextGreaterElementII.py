"""
    503 - Next Greater Element II
    @author oneshan
    @version 1.0 2/6/2017
"""


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = [-1 for _ in range(len(nums))]
        for idx, num in enumerate(nums + nums):
            while (stack and num > nums[stack[-1]]):
                popped = stack.pop()
                ans[popped] = num

            if idx < len(nums):
                stack.append(idx)
        return ans
