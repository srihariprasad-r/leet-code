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
    
# Method 2 - wrong submission
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        s = 0
        c1 = l1
        c2 = l2

        dummy = ListNode(None)
        new = dummy

        while c1 and c2:
            s += c1.val + c2.val
            if c > 0: 
                s += c
                c = 0
            c1 = c1.next
            c2 = c2.next
            s , c = s % 10, s // 10
            new.next = ListNode(s)
            new = new.next
            s = 0

        return dummy.next