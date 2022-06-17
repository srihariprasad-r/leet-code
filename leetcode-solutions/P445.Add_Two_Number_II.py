# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        list1 = []
        list2 = []
        list3 = []
        ret = ListNode(-1)
        cur = ret
                
        while l1:
            list1.append(l1.val)
            l1 = l1.next
                    
        while l2:
            list2.append(l2.val)
            l2 = l2.next                    
        
        minLen = min(len(list1), len(list2))
        
        carry = 0
        
        while minLen > 0:
            sum_1 = 0
            sum_2 = 0
            
            if len(list1) > 0:
                #if list1[-1] or list1[-1] == 0:
                sum_1 = list1[-1]
                list1.pop(-1)
                    
            if len(list2) > 0:                
                #if list2[-1] or list2[-1] == 0:
                sum_2 = list2[-1]
                list2.pop(-1)      
                            
            total = sum_1 + sum_2 + carry
            carry = total // 10
            value = total % 10            
            list3.append(value)            
            minLen -= 1    

        
        while len(list2) > 0:                 
            total = list2[-1] + carry
            carry = total // 10
            value = total % 10                             
            if carry > 0:
                list3.append(value)  
            else:
                list3.append(total)      
            list2.pop(-1)
                
        while len(list1) > 0:
            total = list1[-1] + carry
            carry = total // 10
            value = total % 10            
            if carry > 0:
                list3.append(value)  
            else:
                list3.append(total)  
            list1.pop(-1)                
        
        if carry > 0:
            list3.append(1)                     
        
        while len(list3) > 0:
            cur.next = ListNode(list3[-1])
            cur = cur.next
            list3.pop()
            
        return ret.next
                
        