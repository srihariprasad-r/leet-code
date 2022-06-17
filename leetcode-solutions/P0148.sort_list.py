# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        left= self.getmid(head)
        right = left.next
        left.next = None
        
        return self.merge(self.sortList(head), self.sortList(right))
        
    def getmid(self, head):
        slow, fast = head, head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow
    
    def merge(self, list1, list2):
        dummy = ListNode(-1)
        cur = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                cur.next, list1 = list1, list1.next
            else:
                cur.next, list2 = list2, list2.next
                
            cur = cur.next
            
        if list1:
            cur.next = list1
        
        if list2:
            cur.next = list2

        return dummy.next