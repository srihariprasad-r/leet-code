# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        while curr and curr.next:
            nxt = curr.next.next
            second = curr.next
            
            second.next = curr
            curr.next = nxt
            prev.next = second
            
            prev = curr
            curr = nxt
            
        return dummy.next