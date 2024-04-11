# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(l):
            prev = None
            cur = l

            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            return prev

        def knode(node,c):
            c -= 1
            while c > 0 and node:
                c -= 1
                node = node.next

            return node

        tmp = head
        prev = None

        while tmp:
            k_node = knode(tmp,k)
            if not k_node:
                if prev: prev.next = tmp
                break
            nxt = k_node.next
            k_node.next = None
            r = reverse(tmp)
            if tmp == head:
                head = k_node
            else:
                prev.next = k_node
            prev = tmp
            tmp = nxt

        return head