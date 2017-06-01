"""
    563 - Binary Tree Tilt
    @author oneshan
    @version 1.0 5/31/2017
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tile = 0

        def search(node):
            if not node:
                return 0
            sum_left = search(node.left)
            sum_right = search(node.right)
            self.tile += abs(sum_left - sum_right)
            return node.val + sum_left + sum_right

        search(root)
        return self.tile
