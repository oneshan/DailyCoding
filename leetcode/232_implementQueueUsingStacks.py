class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.aux = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.aux:
            while self.stack:
                self.aux.append(self.stack.pop())
        return self.aux.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.aux:
            return self.stack[0]
        return self.aux[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (not self.stack) and (not self.aux)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
