"""
    235 - Lowest Common Ancestor of a Binary Search Tree
    @author oneshan
    @version 1.0 3/5/2017
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val < q.val:
            minV, maxV = p.val, q.val
        else:
            minV, maxV = q.val, p.val

        while root:
            if root.val < minV:
                root = root.right
            elif root.val > maxV:
                root = root.left
            else:
                return root
