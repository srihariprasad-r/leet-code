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
        l1 = 0
        p1 = headA
        while p1:
            l1 += 1
            p1 = p1.next
  
        l2 = 0
        p2 = headB
        while p2:
            l2 += 1
            p2 = p2.next

        p1 = headA
        p2 = headB
        if l1 < l2:
            change = l2 -l1
            i = 0
            while i < change:
                p2 = p2.next
                i += 1
        else:
            change = l1 -l2
            i = 0
            while i < change:
                p1 = p1.next
                i += 1
        
        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next