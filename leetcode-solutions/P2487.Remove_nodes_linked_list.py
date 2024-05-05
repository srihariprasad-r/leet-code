# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stck = []

        cur = head
        while cur:
            while stck and stck[-1] < cur.val:
                stck.pop()
            stck.append(cur.val)
            cur = cur.next

        dummy = ListNode(None)
        cur = dummy

        while stck:
            val = stck.pop(0)
            cur.next = ListNode(val)
            cur = cur.next

        return dummy.next