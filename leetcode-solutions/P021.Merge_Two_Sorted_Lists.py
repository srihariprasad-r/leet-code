# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(-1);
        head = l3

        if (l1 is None) and not(l2 is None):
            l3.next = l2;
        elif (l2 is None) and not(l1 is None):
            l3.next = l1;
        
        while(not(l1 is None) and not(l2 is None)):
            if(l1.val <= l2.val):
                l3.next = l1
                l1 = l1.next
                #l3 = l3.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
                
            if (l1 is not None):
                l3.next = l1;
            elif (l2 is not None):
                l3.next = l2;
        
        return head.next