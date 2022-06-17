class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        elif root.left is None:
            return self.minDepth(root.right) + 1
        elif root.right is None:
            return self.minDepth(root.left) + 1
        elif root.left is not None and root.right is not None:
            return min(self.minDepth(root.left) , self.minDepth(root.right))  +1
        else:
            return 1