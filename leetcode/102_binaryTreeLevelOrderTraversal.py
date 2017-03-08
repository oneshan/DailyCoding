"""
    102 - Binary Tree Level Order Traversal
    @author oneshan
    @version 1.0 3/7/2017
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        table = {}
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            table.setdefault(level, [])
            table[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        ans = []
        for i in range(level + 1):
            ans.append(table[i])
        return ans
