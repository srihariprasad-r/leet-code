# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #l3 = ListNode(-1)
        node = head
        
        while(node is not None and node.next is not None):
            if (node.val != node.next.val):
                #h.next = h
                node = node.next
            else:
                node.next = node.next.next
        
        return head