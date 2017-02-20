"""
    113 - Path Sum II
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        ans = []
        stack = [(root, [root.val], root.val)]
        while stack:
            node, path, temp_sum = stack.pop()
            if node.left is None and node.right is None:
                if temp_sum == sum:
                    ans.append(path)
            if node.left:
                stack.append([node.left, path + [node.left.val], temp_sum + node.left.val])
            if node.right:
                stack.append([node.right, path + [node.right.val], temp_sum + node.right.val])
        return ans
