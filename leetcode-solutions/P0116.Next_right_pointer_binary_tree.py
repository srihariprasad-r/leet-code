"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def t(self, node1, node2):
        if node1 is None or node2 is None:
            return

        node1.next = node2
        self.t(node1.left, node1.right)
        self.t(node2.left, node2.right)
        self.t(node1.right, node2.left)

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return

        self.t(root.left, root.right)
        return root