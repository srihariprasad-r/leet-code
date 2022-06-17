# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        results = []
        def inorder(root):            
            if root:
                inorder(root.left)
                results.append(root.val)    
                inorder(root.right)
                
        inorder(root)
        
        tnode = ptr = TreeNode(0)
        
        for i in range(len(results)):
            ptr.right = TreeNode(results[i])
            ptr = ptr.right
            
        return tnode.right