# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_node = None
        cur = head
        
        while cur:
            next_node = cur.next
            cur.next = prev_node
            prev_node = cur
            cur = next_node
            
        return prev_node
            