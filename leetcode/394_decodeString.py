"""
    394 - Decode String
    @author oneshan
    @version 1.0 5/26/2017
"""


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for ch in s:
            if ch == ']':
                # pop and get chars inside brackets
                string = ""
                while stack and stack[-1] != '[':
                    string = stack.pop() + string

                # pop '['
                stack.pop()

                # pop and get repeated count
                count = ""
                while stack and stack[-1].isnumeric():
                    count = stack.pop() + count
                count = int(count) if count else 1

                # push back repeated chars
                stack.append(string * count)
            else:
                stack.append(ch)

        ans = ""
        while stack:
            ans = stack.pop() + ans

        return ans


class Solution_2(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        stack.append(["", 0])

        num = ""
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                stack.append(["", int(num)])
                num = ""
            elif ch == ']':
                string, count = stack.pop()
                stack[-1][0] += string * count
            else:
                stack[-1][0] += ch
        return stack[0][0]
