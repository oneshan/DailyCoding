"""
    234 - Palindrome Linked List
    @author oneshan
    @version 1.0 3/5/2017
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

        # Find the middle node of linked list
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse half of linked list
        pre = None
        curr = slow.next
        next = None
        while curr:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        slow.next = pre

        # Compare
        p1, p2 = head, slow.next
        while p2 and p1.val == p2.val:
            if not p2.next:
                return True
            p1 = p1.next
            p2 = p2.next
        return False
