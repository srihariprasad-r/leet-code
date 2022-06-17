"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        q = deque()
        q.append(root)

        while len(q) > 0:
            n = len(q)

            for i in range(n):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)

                if i != n - 1:
                    cur.next = q[0]

        return root