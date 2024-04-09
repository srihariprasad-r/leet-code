# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        st = set()
        tmp = head

        while tmp.next:
            if tmp.val == tmp.next.val:
                st.add(tmp.val)
            tmp = tmp.next

        dummy = ListNode(101)
        dummy.next = head
        tmp = dummy

        while tmp.next:
            if tmp.val in st:
                while tmp.next and tmp.next.val in st:
                    tmp.next = tmp.next.next
            else:
                if tmp.next.val in st:
                    tmp.next = tmp.next.next
                else:
                    tmp = tmp.next

        return dummy.next
        
