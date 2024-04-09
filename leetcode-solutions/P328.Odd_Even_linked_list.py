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

# Method 2 - almost same
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        first = head
        second = head.next
        c = second

        while first.next and second.next:
            first.next = first.next.next
            second.next = second.next.next
            first = first.next
            second = second.next

        first.next = c

        return head