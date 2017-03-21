"""
    543 - Diameter of Binary Tree
    @author oneshan
    @version 1.0 3/20/2017
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 1

        def recursion(node):
            if node is None:
                return 0
            l = recursion(node.left)
            r = recursion(node.right)
            self.ans = max(self.ans, 1 + l + r)
            return 1 + max(l, r)
        recursion(root)
        return self.ans - 1
