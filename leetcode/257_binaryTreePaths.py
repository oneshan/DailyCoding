"""
    257 - Binary Tree Paths
    @author oneshan
    @version 1.0 2/19/2017
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        if root is None:
            return []

        ans = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if node.left is None and node.right is None:
                ans.append(path)
            if node.left:
                stack.append([node.left, path + "->%d" % node.left.val])
            if node.right:
                stack.append([node.right, path + "->%d" % node.right.val])
        return ans
