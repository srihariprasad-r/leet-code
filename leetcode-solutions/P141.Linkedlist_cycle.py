# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """       
        if (head is None):
            return False
        
        p1 = head
        p2 = head
        while(p1 is not None and p1.next is not None):
            p1 = p1.next.next
            p2 = p2.next
            
            if p1 == p2:
                return True
        return False

# Method 2 - wrong submission
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return False
        
        fast = head
        slow = head

        while fast.next.next and slow.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow: return True

        return False
        