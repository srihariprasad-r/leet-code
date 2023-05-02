# Definition for a binary tree node.
# wrong submission

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root1):
            if root1 is None: return False

            return dfs(root, subRoot) or dfs(root.left, subRoot) or dfs(root.right, subRoot)

        def dfs(node, subnode):
            if node is None or subnode is None: 
                return node == subnode

            return node.val == subnode.val and \
                dfs(node.left, subnode.left) and dfs(node.right, subnode.right)

        return isSame(root)