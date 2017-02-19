"""
    112 - Path Sum
    @author oneshan
    @version 1.0 2/18/2017
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    """ Using stack """
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        stack = [(root, sum)]
        while stack:
            node, val = stack.pop()
            val -= node.val

            if val == 0 and not node.left and not node.right:
                return True

            if node.left:
                stack.append((node.left, val))
            if node.right:
                stack.append((node.right, val))

        return False


class Solution_2(object):
    """ Recursive version """
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        if root.val == sum and not root.left and not root.right:
            return True

        return (self.hasPathSum(root.left, sum - root.val) or
                self.hasPathSum(root.right, sum - root.val))
