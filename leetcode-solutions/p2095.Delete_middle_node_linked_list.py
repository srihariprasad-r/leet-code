# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        c = 0
        tmp = head

        while tmp.next:
            c += 1
            tmp = tmp.next

        if c == 0: return head.next

        tmp = head
        t = 0
        n = c // 2 if c % 2 else (c//2)-1

        while tmp.next:
            if t == n:
                tmp.next = tmp.next.next if tmp.next.next else None
            else:
                tmp = tmp.next
            t += 1

        return head