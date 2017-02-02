"""
    273 - Delete Node in a Linked List
    @author oneshan
    @version 1.0 2/1/2017
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None or node.next is None:
            node = None
            return
        
        node.val = node.next.val
        node.next = node.next.next
