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
        e = prev

        greater = ListNode(-101)
        m = greater

        while cur:
            nxt = cur.next
            if cur.val < x:
                e.next = cur
                e = e.next
            else:
                m.next = cur
                m = m.next
            cur = nxt

        m.next = None

        a = prev
        while a.next:
            a = a.next
        a.next = greater.next
        
        return prev.next