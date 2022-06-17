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