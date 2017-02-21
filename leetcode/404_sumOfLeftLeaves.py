"""
    404 - Sum of Left Leaves
    @author oneshan
    @version 1.0 2/20/2017
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        ans = 0
        stack = [(root, False)]

        while stack:
            node, isLeft = stack.pop()
            if isLeft and node.left is None and node.right is None:
                ans += node.val
            if node.left:
                stack.append((node.left, True))
            if node.right:
                stack.append((node.right, False))
        return ans
