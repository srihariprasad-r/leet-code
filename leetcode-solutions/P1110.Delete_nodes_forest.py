# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        def f(node):
            if not node:
                return None

            # rN = TreeNode(node.val)
            node.left = f(node.left)
            node.right = f(node.right)    

            if node.val in to_delete:
                if node.left: res.append(node.left)
                if node.right: res.append(node.right)
                node = None     

            return node

        root = f(root)
        if root: res.append(root)
        return res