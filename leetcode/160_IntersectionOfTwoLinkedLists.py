"""
    160 - Intersection of Two Linked Lists
    @author oneshan
    @version 1.0 3/3/2017
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        p1, p2 = headA, headB
        len1, len2 = 0, 0

        while p1 is not None:
            p1 = p1.next
            len1 += 1
        while p2 is not None:
            p2 = p2.next
            len2 += 1

        p1, p2 = headA, headB
        for i in range(len1 - len2):
            p1 = p1.next
        for i in range(len2 - len1):
            p2 = p2.next

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
