# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l1 = list1

        c = 0

        while l1.next:
            c += 1
            l1 = l1.next

        l1 = list1
        c1 = 1
        while c1 != a:
            l1 = l1.next
            c1 += 1


        last = list1
        m = None
        c1 = 0
        while last.next:
            last = last.next
            c1 += 1       
            if c1 == b:
                m  = last.next
                break

        l1.next = None
        d = list1
        while d.next:
            d = d.next

        c = list2
        while c.next:
            c = c.next

        c.next = m
        d.next = list2

        return list1   