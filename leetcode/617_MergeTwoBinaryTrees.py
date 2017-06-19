"""
    617 - Merge Two Binary Trees
    @author oneshan
    @version 1.0 6/18/2017
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def merge(t1, t2):
            if t1 and t2:
                r1, r2, l1, l2 = t1.right, t2.right, t1.left, t2.left
            elif t1:
                r1, r2, l1, l2 = t1.right, None, t1.left, None
            elif t2:
                r1, r2, l1, l2 = None, t2.right, None, t2.left
            else:
                return None
            node = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
            node.left = merge(l1, l2)
            node.right = merge(r1, r2)
            return node

        root = merge(t1, t2)
        return root
