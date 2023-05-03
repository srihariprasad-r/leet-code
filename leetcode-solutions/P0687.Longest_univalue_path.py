# wrong submission

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node, val, ln=0):
            if node is None:
                return ln

            return max(dfs(node.left, node.val if node.val != val else val,
                           ln + 1 if node.val == val else ln),
                       dfs(node.right, node.val if node.val != val else val,
                           ln + 1 if node.val == val else ln))

        return max(dfs(root.left, root.val, 0), dfs(root.right, root.val, 0))