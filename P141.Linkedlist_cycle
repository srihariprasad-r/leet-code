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
            