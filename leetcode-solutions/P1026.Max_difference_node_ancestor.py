# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:   
        self.mx = 0 
        def mx(node, mn_s):
            if not node:
                return mn_s

            left_mn_s = mx(node.left, mn_s if node.val > mn_s else node.val)
            right_mn_s  = mx(node.right, mn_s if node.val > mn_s else node.val)
            
            self.mx = max(self.mx, abs(node.val - min(left_mn_s, right_mn_s)))            

            return min(left_mn_s, right_mn_s)

        mx(root, float('inf'))
        return self.mx