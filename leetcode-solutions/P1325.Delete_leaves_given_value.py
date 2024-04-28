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
            if rN.left and rN.left.val == target and rN.left.left is None and rN.left.right is None:
                rN.left  = None
            rN.right = f(node.right)       
            if rN.right and rN.right.val == target and rN.right.left is None and rN.right.right is None:
                rN.right  = None                    
                       
            return rN

        nr = f(root)
        return f(nr)