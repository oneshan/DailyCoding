# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    """ Recursive version"""
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(node):
            if node:
                inorder(node.left)
                ans.append(node.val)
                inorder(node.right)
        ans = []
        inorder(root)
        return ans


class Solution_2(object):
    """ Iterative Version"""
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        stack = []
        current = root

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                ans.append(current.val)
                current = current.right
            else:
                break

        return ans
