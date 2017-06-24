"""
    606 - Construct String from Binary Tree
    @author oneshan
    @version 1.0 6/22/2017
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def traverse(node):
            if not node:
                return ""
            if not node.left and not node.right:
                return str(node.val)
            if not node.right:
                return "{}({})".format(node.val, traverse(node.left))
            return "{}({})({})".format(node.val, traverse(node.left), traverse(node.right))
        return traverse(t)
