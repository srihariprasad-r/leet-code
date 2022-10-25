# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = []

        for node in lists:
            if node:
                heapq.heappush(pq, (node.val, node))
            
        dummy = ListNode()
        head = dummy
        
        while pq:
            val, node = heapq.heappop(pq)
            head.next = node
            if node.next:
                heapq.heappush(pq, (node.next.val, node.next))
                
            head = head.next
            
        return dummy.next