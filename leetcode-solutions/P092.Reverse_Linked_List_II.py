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

# Method 2 - TLE
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head: return None

        a = head
        l = 1
        
        while a.next:
            l += 1
            a = a.next
        
        if l == 1: return head

        a = head
        c = 1

        while a.next:
            if c < left:
                c += 1
            else: break
            a = a.next

        tmp = a
        prev = None

        while tmp:
            if c <= right:
                c += 1
            else:
                r = tmp
                break
            cur = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = cur

        a = head
        a.next = prev

        if r:
            while a.next:
                a = a.next
            a.next = r

        return head