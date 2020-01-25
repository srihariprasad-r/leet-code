# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSymmentric(root.left, root.right)
    
    def isSymmentric(self,left, right):
        if ((left is None) or (right is None)):
            return left == right
        
        if left.val != right.val:
            return False
        
        return self.isSymmentric(left.left, right.right) and self.isSymmentric(left.right, right.left)
            