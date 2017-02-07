"""
    020 - Valid Parentheses
    @author oneshan
    @version 1.0 2/6/2017
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            if ch in ')}]':
                if not stack:
                    return False
                if match[ch] != stack.pop():
                    return False
        if stack:
            return False
        return True
        
