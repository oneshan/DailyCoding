"""
    445 - Add Two Numbers II
    @author oneshan
    @version 1.0 2/4/2017
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
        # Get length of Linked List l1, l2
        len1, len2 = 0, 0
        temp, temp2 = l1, l2
        while (temp or temp2):
            if temp:
                temp = temp.next
                len1 += 1
            if temp2:
                temp2 = temp2.next
                len2 += 1

        # sum two linked list without carry
        head = ListNode(0)
        current = head
        size = max(len1, len2)
        while size:
            val = 0
            if size <= len1:
                val += l1.val
                l1 = l1.next
            if size <= len2:
                val += l2.val
                l2 = l2.next
            current.next = ListNode(val)
            current = current.next
            size = size - 1

        # handle carry
        prev = head
        while prev:
            # current is the digit after 9s
            current = prev.next
            while current and current.val == 9:
                current = current.next

            while prev != current:
                # carry all 9s before current digit
                if current and current.val > 9:
                    prev.val += 1
                    prev.next.val -= 10
                prev = prev.next

        if head.val:
            return head
        return head.next
