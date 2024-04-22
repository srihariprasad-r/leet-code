# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        t = head
        p1 = head
        p2 = head
        
        ln = 1
        while t.next:
            t = t.next
            ln += 1
            
        cnt = 1
        while p1 and cnt != k:
            p1 = p1.next
            cnt += 1

        cnt = 0
        while p2 and cnt != ln - k:
            p2 = p2.next
            cnt += 1
        
        
        tmp = p2.val
        p2.val = p1.val
        p1.val = tmp
        
        return head

# Method 2 - almost same
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        if not head.next: return head

        l = 1

        cur = head
        while cur.next:
            l += 1
            cur = cur.next

        prev_first = None
        prev_last = None

        m = head
        cur = head
        i = 1
        while cur:
            if i == k:
                prev_first = cur
                break
            cur = cur.next
            i += 1
        
        i = 0
        cur = head
        while cur:
            if i == l-k:
                prev_last = cur
                break
            cur = cur.next
            i += 1

        prev_first.val , prev_last.val =  prev_last.val,  prev_first.val

        return head
# Method 3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt = 0
        cur = head

        while cur:
            cur = cur.next
            cnt += 1

        def get_knode(node, l):
            while l > 0 and node:
                node = node.next
                l -= 1
            
            return node

        cur = head

        kth_node = get_knode(cur, k-1)
        last_kth_node = get_knode(cur, cnt-k)
        
        kth_node.val, last_kth_node.val = last_kth_node.val, kth_node.val

        return head