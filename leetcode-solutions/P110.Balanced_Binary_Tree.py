# Definition for a binary tree node.
#class TreeNode(object):
#    def __init__(self, x, left= None, right= None):
#        self.val = x
#        self.left = left
#        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """        
        if root is None:
            return True
        else:
            if abs(self.maxdepth(root.left) - self.maxdepth(root.right)) > 1:
                return False
            else:                        
                return self.isBalanced(root.left) and self.isBalanced(root.right)
            
    def maxdepth(self, root):
        if root is None:
            return 0
        else:
            return max(self.maxdepth(root.left), self.maxdepth(root.right)) + 1