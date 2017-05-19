"""
    199 - Binary Tree Right Side View
    @author oneshan
    @version 1.0 5/18/2017
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        self.ans = []
        self.layer = 0

        def dfs(node, layer):
            if layer == self.layer:
                self.layer += 1
                self.ans.append(node.val)
            if node.right:
                dfs(node.right, layer + 1)
            if node.left:
                dfs(node.left, layer + 1)

        dfs(root, 0)
        return self.ans
