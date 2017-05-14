"""
    129 - Sum Root to Leaf Numbers
    @author oneshan
    @version 1.0 5/14/2017
"""


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        sum = 0
        stack = [(root, 0)]
        while stack:
            curr, value = stack.pop()
            value = value * 10 + curr.val
            if not curr.left and not curr.right:
                sum += value
                continue
            if curr.right:
                stack.append((curr.right, value))
            if curr.left:
                stack.append((curr.left, value))
        return sum
