# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def f(node, pt, a, d):
            if not node: return None, -1

            if node.val == a:
                return pt.val, d

            parent = None
            k = -1
            parent, k = f(node.left, node, a, d+1)

            if parent is None and k == -1:
                parent, k = f(node.right, node, a, d + 1)

            return parent, k

        x_parent = f(root, root, x, 0)
        y_parent = f(root, root, y, 0)

        if ((x_parent[0] != y_parent[0]) and (x_parent[1] == y_parent[1])):
            return True

        return False