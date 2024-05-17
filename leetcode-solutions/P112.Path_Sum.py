class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """        
        if root is None:
            return False
        elif (root.left is None and root.right is None and sum - root.val == 0):
            return True
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False

        if root and not root.left and not root.right:
            if root.val == targetSum: return True
            return False
            
        def f(node, s):
            if not node: return False

            if (node and not node.left and not node.right):
                if s + node.val == targetSum: return True
                return False  

            l = f(node.left, s + node.val)          
            r = f(node.right, s + node.val)                 
            
            return l or r
        
        return f(root.left, root.val) or f(root.right, root.val)