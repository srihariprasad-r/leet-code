# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import collections
        d = collections.defaultdict(int)

        s = 0
        dummy = ListNode(None)
        h = dummy
        prev_s = 0

        c = head
        while c.next:
            while c.val != 0:
                s += c.val
                c = c.next
            if s > 0:
                h.next = ListNode(s)
                h = h.next
                s = 0
            if c.next: c = c.next

        return dummy.next