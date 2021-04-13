# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        p1 = list1
        p2 = list1
        
        cnt = 1
        while p1 and cnt != a:
            p1 = p1.next
            cnt += 1
        
        cnt = 0
        while p2 and cnt != b:
            p2 = p2.next
            cnt += 1
        
        p1.next = list2
        
        while list2.next:
            list2 = list2.next
        
        list2.next = p2.next
        
        return list1