"""
    515 - Find Largest Value in Each Tree Row
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
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        ans = []
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            if len(ans) < level + 1:
                ans.append(node.val)
            else:
                ans[level] = max(ans[level], node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return ans
