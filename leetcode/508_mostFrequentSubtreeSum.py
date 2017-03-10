"""
    508 - Most Frequent Subtree Sum
    @author oneshan
    @version 1.0 3/9/2017
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def recur(node, table):
            if node is None:
                return 0
            sum = node.val + recur(node.left, table) + recur(node.right, table)
            table[sum] = table.get(sum, 0) + 1
            return sum

        table = {}
        recur(root, table)

        ans, maxFreq = [], 0
        for sum in table:
            if table[sum] > maxFreq:
                ans = [sum]
                maxFreq = table[sum]
            elif table[sum] == maxFreq:
                ans.append(sum)
        return ans
