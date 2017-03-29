"""
    538 - Convert BST to Greater Tree
    @author oneshan
    @version 1.0 3/28/2017
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        sum, node, stack = 0, root, []
        while True:
            while node:
                stack.append(node)
                node = node.right
            if not stack:
                break
            node = stack.pop()
            sum = node.val = node.val + sum
            node = node.left
        return root


class Solution_2(object):
    sum = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.right:
            self.convertBST(root.right)
        self.sum = root.val = root.val + self.sum
        if root.left:
            self.convertBST(root.left)
        return root
