"""
    002 - Add Two Numbers
    @author oneshan
    @version 1.0 1/30/2017
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        last = None

        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum = carry + v1 + v2
            carry = 1 if sum >= 10 else 0
            sum = sum % 10

            temp = ListNode(sum)
            if head is None:
                head = temp
            else:
                last.next = temp
            last = temp

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            last.next = ListNode(carry)

        return head
