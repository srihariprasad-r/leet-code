# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        
        new_node = ListNode(-1)
        new_node.next = head
        head = new_node

        while new_node.next:            
            if new_node.next.val == val:
                new_node.next = new_node.next.next
            else:
                new_node = new_node.next

        return head.next
            