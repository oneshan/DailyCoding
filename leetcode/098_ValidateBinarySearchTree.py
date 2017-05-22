"""
    098 - Validate Binary Search Tree
    @author oneshan
    @version 1.0 5/22/2017
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        self.arr = []

        def inorder(node):
            if node.left:
                inorder(node.left)
            self.arr.append(node.val)
            if node.right:
                inorder(node.right)

        inorder(root)
        pre = float('-inf')
        for val in self.arr:
            if pre >= val:
                return False
            pre = val
        return True


class Solution_2(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        self.prev = float('-inf')
        self.ans = True

        def inorder(node):
            if not self.ans:
                return

            if node.left:
                inorder(node.left)

            if self.prev >= node.val:
                self.ans = False
            self.prev = node.val

            if node.right:
                inorder(node.right)

        inorder(root)
        return self.ans
