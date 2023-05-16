# wrong submission

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, val, ln=0):
            if node is None:
                return ln

            newval = node.val if node.val != val else val
            ln = ln + 1 if node.val == val else ln

            return max(dfs(node.left, newval, ln), dfs(node.right, newval, ln))

        return dfs(root.left, root.val, 0) + dfs(root.right, root.val, 0)

# Method 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.mx = 0

        def dfs(node):
            if node is None:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            l = l + 1 if node.left and node.left.val == node.val else 0
            r = r + 1 if node.right and node.right.val == node.val else 0

            self.mx = max(self.mx, l + r)

            return max(l, r)

        dfs(root)

        return self.mx
