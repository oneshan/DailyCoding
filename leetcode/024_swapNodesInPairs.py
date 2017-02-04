"""
    024 - Swap Nodes in Pairs
    @author oneshan
    @version 1.0 2/3/2017
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        while temp:
            if temp.next is None:
                break
            temp.val, temp.next.val = temp.next.val, temp.val
            temp = temp.next.next

        return head
