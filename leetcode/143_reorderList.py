"""
    143 - Reorder List
    @author oneshan
    @version 1.0 6/1/2017
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """

        # Split list
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow:
            head2 = slow.next
            slow.next = None
        else:
            head2 = None

        # Reverse list
        curr, pre = head2, None
        while curr:
            temp = curr.next
            curr.next = pre
            pre, curr = curr, temp
        head2 = pre

        # Merge list
        p1, p2 = head, head2
        while p2:
            temp = p1.next
            p1.next = p2
            p2 = p2.next
            p1.next.next = temp
            p1 = temp
