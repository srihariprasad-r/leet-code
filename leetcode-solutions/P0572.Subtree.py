# Definition for a binary tree node.
# wrong submission

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node, subnode):
            if node is None or subnode is None:
                return True

            return node.val == subnode.val and \
                dfs(node.left, subnode.left) and dfs(node.right, subnode.right)

        return dfs(root, subRoot)