# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        el = []
        stck = []
        c = 0

        cur = head

        while cur:
            c += 1
            el.append(cur.val)
            cur = cur.next

        nge = [0] *c
        
        for i in range(len(el)):
            while stck and el[stck[-1]] < el[i]:                
                nge[stck.pop()] = el[i]
            stck.append(i)                                   

        return nge