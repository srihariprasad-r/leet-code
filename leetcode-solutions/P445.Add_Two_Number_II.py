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
                
# Method 2 - wrong submission
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ln1 = 0
        ln2 = 0

        c1 = l1
        while c1:
            c1 = c1.next
            ln1 += 1
        
        c2= l2
        while c2:
            c2 = c2.next
            ln2 += 1

        c1 = l1
        c2 = l2

        # prev2 = None
        # while c2:
        #     tmp = c2.next
        #     c2.next = prev2
        #     prev2 = c2
        #     c2 = tmp
        #     ln2 += 1
        
        if ln1 != ln2:
            d = ListNode(0)
            t = d
            t.next = l1 if ln1 < ln2 else l2


        dummy = ListNode(None)
        end = dummy
        c = 0

        if ln1 < ln2:
            c1 = t 
        elif ln1 > ln2:
            c2 = t

        while c1 and c2:
            s = c1.val + c2.val
            if c > 0:
                s += c
                c = 0
            end.next = ListNode(s)
            end = end.next
            c1 = c1.next
            c2 = c2.next
            s = 0

        e = dummy.next
        prev = None
        while e:
            if e.val > 9:
                prev.val +=  e.val//10
                e.val = 0
            prev = e
            e = e.next

        return dummy.next