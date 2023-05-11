# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(i, p):
            if not i or not p:
                return

            v = p.pop()
            idx = i.index(v)
            root = TreeNode(v)
            root.right = dfs(i[idx+1:], p)
            root.left = dfs(i[:idx], p)

            return root

        return dfs(inorder, postorder)