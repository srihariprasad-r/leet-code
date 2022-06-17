# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        
        count = 1
        
        while count != m:
            prev = prev.next
            count += 1
            
        cur = prev.next               
                
        for _ in range(0,n-m):
            if cur.next:
                NEXT = cur.next    
                cur.next = NEXT.next
                NEXT.next = prev.next
                prev.next = NEXT                
        
        return dummy.next