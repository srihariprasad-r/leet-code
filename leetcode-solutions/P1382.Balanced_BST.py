# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.arr = []
        def inorder(node):
            if node.left: inorder(node.left)
            self.arr.append(node.val)
            if node.right: inorder(node.right)
            return self.arr
        
        inorder(root)

        def dfs(arr, l, r):
            if l > r: return None
            if l == r: return TreeNode(arr[l])
            mid = l + (r-l)//2
            root = TreeNode(arr[mid])
            root.left = dfs(arr, l, mid - 1)
            root.right = dfs(arr, mid + 1, r)
            return root

        return dfs(self.arr, 0, len(self.arr)-1)