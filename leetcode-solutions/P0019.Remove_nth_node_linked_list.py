# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = head
        second = head
        
        while n > 0:
            first = first.next
            n -= 1

        if not(first):
            return head.next
        else:
            while first.next:
                first = first.next
                second = second.next
                
        second.next = second.next.next
        
        return head

# Method 2 - wrong submission
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if ((not head) or (head and not head.next and n == 1)): return None
    
        c = 1
        tmp = head

        while tmp.next:
            tmp = tmp.next
            c += 1

        t = 0
        prev = None
        tmp = head
        
        while t < c - n :
            prev = tmp
            tmp = tmp.next
            t += 1

        prev.next = tmp.next

        return head