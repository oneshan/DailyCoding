"""
    107 - Binary Tree Level Order Traversal II
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
    def levelOrderBottom(self, root):
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
        while level >= 0:
            ans.append(table[level])
            level -= 1
        return ans
