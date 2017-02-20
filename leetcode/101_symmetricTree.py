"""
    101 - Symmetric Tree
    @author oneshan
    @version 1.0 2/9/2017
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def compare(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            return (compare(left.left, right.right) and
                    compare(left.right, right.left))

        return compare(root, root)


class Solution_2(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        tree1 = []
        tree2 = []

        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                tree1.append(None)
            else:
                tree1.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                tree2.append(None)
            else:
                tree2.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return (tree1 == tree2)
