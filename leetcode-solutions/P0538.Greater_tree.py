# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.s = 0

        def dfs(node):
            if not node:
                return 0

            dfs(node.right)
            node.val += self.s
            self.s = node.val
            dfs(node.left)

        dfs(root)

        return root
