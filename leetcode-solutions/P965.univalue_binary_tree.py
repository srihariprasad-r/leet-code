# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def func1(node, val):
            if node is None:
                return True
            elif node.val != val:
                return False
            
            return func1(node.left, val) and func1(node.right, val)
        
        return func1(root, root.val)