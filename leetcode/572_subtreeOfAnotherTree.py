"""
    572 - Subtree of Another Tree
    @author oneshan
    @version 1.0 5/17/2017
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isSameTree(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)

        if isSameTree(s, t):
            return True
        if s.left and self.isSubtree(s.left, t):
            return True
        if s.right and self.isSubtree(s.right, t):
            return True
        return False


class Solution_2(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def preorder(curr):
            return '$' if curr is None else (
                '#' + str(curr.val) + preorder(curr.left) + preorder(curr.right))
        return preorder(t) in preorder(s)
