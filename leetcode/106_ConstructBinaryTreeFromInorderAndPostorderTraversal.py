"""
    106 - Construct Binary Tree from Inorder and Postorder Traversal
    @author oneshan
    @version 1.0 3/25/2017
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None

        rootIdx = inorder.index(postorder.pop())
        root = TreeNode(inorder[rootIdx])
        root.right = self.buildTree(inorder[rootIdx + 1:], postorder)
        root.left = self.buildTree(inorder[:rootIdx], postorder)
        return root
