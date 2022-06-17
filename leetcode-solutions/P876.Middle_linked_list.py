# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lenlist = 0
        
        l1 = head
        
        while l1:
            lenlist += 1
            l1 = l1.next
        
        middle = lenlist // 2
        
        def findnext(lst, cntr):  
            lenlist = 0
            while lst and lenlist < cntr:
                lenlist += 1
                lst = lst.next
            
            return lst
        
        return findnext(head, middle)