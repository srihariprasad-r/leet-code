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