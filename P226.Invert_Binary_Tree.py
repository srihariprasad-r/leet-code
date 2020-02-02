class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
                
        self.tempnode = root.left
        root.left = root.right
        root.right = self.tempnode
        
        self.invertTree(root.left)
        self.invertTree(root.right)        
        
        return root