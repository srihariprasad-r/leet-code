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
    
# Method 2 - wrong submission
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        dummy = ListNode(None)
        end = dummy
        p = 1
        q = 1

        c1 = list1
        c2 = list2
        while c1 and c2:
            if c1.val > c2.val:
                end.next = ListNode(c2.val)
                c2 = c2.next
            elif c1.val < c2.val:
                end.next = ListNode(c1.val)
                c1 = c1.next
            else:
                end.next = ListNode(c1.val)
                end = end.next
                end.next = ListNode(c2.val)
                c1 = c1.next
                c2 = c2.next
            end = end.next

        return dummy.next