# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self.carry = 0
        self.total = 0
        self.val = 0 
        l3 = ListNode(0)           
        ret = l3
        while (l1 or l2):
            self.sum1 = 0
            self.sum2 = 0            
            if l1:
                self.sum1 += l1.val
                l1 = l1.next                        
            if l2:
                self.sum2 += l2.val
                l2 = l2.next
                
            self.total = self.sum1 + self.sum2 + self.carry
            self.carry = self.total // 10
            self.val = self.total % 10
            l3.next = ListNode(self.val)
            l3 = l3.next
            
        if self.carry > 0:
            l3.next = ListNode(1)
            l3 = l3.next
        
        return ret.next