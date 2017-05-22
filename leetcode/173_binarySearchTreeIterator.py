"""
    173 - Binary Search Tree Iterator
    @author oneshan
    @version 1.0 5/22/2017
"""


# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.arr = []
        self.ptr = 0

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.arr.append(node.val)
            inorder(node.right)
        inorder(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.ptr < len(self.arr)

    def next(self):
        """
        :rtype: int
        """
        value = self.arr[self.ptr]
        self.ptr += 1
        return value


class BSTIterator_2(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.ptr = 0

        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        tmp = node.right
        while tmp:
            self.stack.append(tmp)
            tmp = tmp.left
        return node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
