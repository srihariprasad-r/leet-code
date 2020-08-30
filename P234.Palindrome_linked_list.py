from copy import copy
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head is None:
            return True
        if head.next is None:
            return True
        
        values = []
        while head:
            values.append(head.val)
            head = head.next

        i = 0
        j = len(values) - 1
            
        while i < j:            
            if int(values[i]) != int(values[j]):
                return False
            else:            
                i += 1
                j -= 1           
            
        return True
        
        