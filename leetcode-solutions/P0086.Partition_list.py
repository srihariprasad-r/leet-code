# wrong submission

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        cur = head

        prev = ListNode(-101)
        prev.next = head
        e = prev.next

        greater = ListNode(-101)
        m = greater

        while cur:
            nxt = cur.next
            if cur.val >= x and nxt.val >= x:   
                m.next = cur
                m = m.next
                m.next = nxt
                cur = cur.next.next
                m = m.next
            else:
                if cur.val < x:
                    e.next = cur
                else:
                    m.next = cur
                    m = m.next
                    if nxt.val < x: m.next = None
                    e = e.next
                cur = nxt

        a = prev
        while a.next:
            a = a.next
        a.next = greater.next
        
        return prev.next