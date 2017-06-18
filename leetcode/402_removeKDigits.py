"""
    402 - Remove K Digits
    @author oneshan
    @version 1.0 6/16/2017
"""


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for n in num:
            while stack and n < stack[-1] and k:
                stack.pop()
                k -= 1
            stack.append(n)
        return "".join(stack[:len(stack) - k]).lstrip('0') or '0'
