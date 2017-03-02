"""
    513 - Find Bottom Left Tree Value
    @author oneshan
    @version 1.0 3/1/2017
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [(root, 0)]
        maxLayer, ans = 0, root.val
        while queue:
            node, layer = queue.pop(0)
            if layer > maxLayer:
                maxLayer = layer
                ans = node.val
            if node.left:
                queue.append((node.left, layer + 1))
            if node.right:
                queue.append((node.right, layer + 1))
        return ans
