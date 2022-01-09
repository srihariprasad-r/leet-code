# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.lst = []
        
        while head:
            self.lst.append(head.val)
            head = head.next 

    def getRandom(self):
        """
        :rtype: int
        """
        from random import random
        return random.choice(self.lst)

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()