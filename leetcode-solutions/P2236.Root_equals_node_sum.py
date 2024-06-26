# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 0
        
        lsum = root.left.val
        rsum = root.right.val

        return root.val == lsum + rsum