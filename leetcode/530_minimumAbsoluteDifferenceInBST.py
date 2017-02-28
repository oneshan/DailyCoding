"""
    530 - Minimum Absolute Difference in BST
    @author oneshan
    @version 1.0 2/27/2017
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        def inorder(root, arr):
            if root is None:
                return
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)

        arr = []
        inorder(root, arr)

        ans = arr[-1] - arr[0]
        for i in range(1, len(arr)):
            ans = min(ans, arr[i] - arr[i - 1])
        return ans


class Solution_2(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = float('inf')
        self.prev = None

        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            if self.prev is not None:
                self.ans = min(self.ans, root.val - self.prev)
            self.prev = root.val
            inorder(root.right)

        inorder(root)
        return self.ans
