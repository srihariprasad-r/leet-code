# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """       
        if head is None:
            return None
        
        p1 = head
        p2 = head.next
        p3 = p2
        
        while p2 is not None and p2.next is not None:
            p1.next = p2.next
            p1 = p1.next
            p2.next = p1.next
            p2 = p2.next
            
        p1.next = p3
        
        return head