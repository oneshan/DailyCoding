"""
    110 - BalancedBinaryTree
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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def getDepth(node):
            if node is None:
                return 0
            return 1 + max(getDepth(node.left), getDepth(node.right))

        if root is None:
            return True

        stack = [root]
        while stack:
            node = stack.pop()
            diff = getDepth(node.right) - getDepth(node.left)
            if abs(diff) > 1:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True


class Solution_2(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def getDepth(node):
            if node is None:
                return 0, True
            lDepth, lBalance = getDepth(node.left)
            if not lBalance:
                return 0, False
            rDepth, rBalance = getDepth(node.right)
            if not rBalance:
                return 0, False
            if abs(lDepth - rDepth) > 1:
                return 0, False
            return 1 + max(lDepth, rDepth), True

        tDepth, tBalance = getDepth(root)
        return tBalance
