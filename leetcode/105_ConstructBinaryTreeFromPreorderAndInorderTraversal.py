"""
    105 - Construct Binary Tree from Preorder and Inorder Traversal
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        rootIdx = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:rootIdx + 1], inorder[:rootIdx])
        root.right = self.buildTree(preorder[rootIdx + 1:], inorder[rootIdx + 1:])
        return root
