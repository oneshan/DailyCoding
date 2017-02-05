"""
    082 - Remove Duplicates from Sorted List II
    @author oneshan
    @version 1.0 2/4/2017
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        res.next = head

        prev = res
        while prev.next:
            current = prev.next
            isDup = False
            while current and current.next:
                if current.val == current.next.val:
                    current.next = current.next.next
                    isDup = True
                else:
                    break
            if isDup:
                prev.next = prev.next.next
            else:
                prev = prev.next

        return res.next
