"""
    155 - Min Stack
    @author oneshan
    @version 1.0 2/14/2017
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.minstack:
            minValue = x
        else:
            minValue = min(x, self.minstack[-1])

        self.minstack.append(minValue)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.minstack.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
