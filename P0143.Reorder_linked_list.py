# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """      
        if head is None or head.next is None:
            return None
        
        l1 = head
        p1 = head   
        p2 = head
        prev = None
        
        while p2 and p2.next:
            prev = p1                  
            p1 = p1.next      
            p2 = p2.next.next
        
        prev.next = None
        
        cur = None
        
        while p1:
            tmp = p1.next
            p1.next = cur
            cur = p1
            p1 = tmp                
        
        while l1:          
            a = l1.next
            b = cur.next
            l1.next = cur            
            if a is None:
                break
            cur.next = a
            l1 = a
            cur = b

            
        
        