"""
    501 - Find Mode in Binary Search Tree
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
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        self.ans = []
        self.val = None
        self.count = 1
        self.maxCount = 1

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.val is None:
                self.val, self.ans = node.val, [node.val]
            else:
                if node.val == self.val:
                    self.count += 1
                else:
                    self.count = 1
                    self.val = node.val
                if self.count > self.maxCount:
                    self.ans = [self.val]
                    self.maxCount = self.count
                elif self.count == self.maxCount:
                    self.ans.append(self.val)

            inorder(node.right)

        inorder(root)
        return self.ans
