# wrong submission
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        rN = None
        def f(node):
            if not node: return
            
            rN = None       

            if node.val == target and not node.left and not node.right:
                return None   
                
            rN = TreeNode(node.val)                                     
            rN.left = f(node.left)
            rN.right = f(node.right)               
                       
            return rN

        return f(root)