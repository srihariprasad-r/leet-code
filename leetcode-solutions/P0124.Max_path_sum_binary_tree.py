# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.mx = float('-inf')
        def dfs(node):
            if not node: return 0
            
            l = max(0, dfs(node.left))
            r = max(0, dfs(node.right))
            self.mx = max(self.mx, l + r + node.val)
            
            return max(l, r)  + node.val

        dfs(root)

        return self.mx