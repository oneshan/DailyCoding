"""
    092 - Reverse Linked List II
    @author oneshan
    @version 1.0 2/3/2017
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head

        res = ListNode(0)
        res.next = head

        left = res
        for i in range(m - 1):
            left = left.next

        current = left.next
        prev = None
        for i in range(n - m + 1):
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        left.next.next = current
        left.next = prev
        return res.next
