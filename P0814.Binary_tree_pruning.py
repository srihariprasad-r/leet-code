# Wrong submission

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None

        if root.val == 0:
            if (root.left and root.left.val == 0) and (root.right and root.right.val == 0):
                return None

            if not root.left and not root.right:
                return None

            # if ((not root.left and root.right and root.right.val == 0)\
            #     or (not root.right and root.left and root.left.val == 0)):
            #     return None

            # if root.left and root.left.val == 1:
            #     return self.pruneTree(root.left)
            # elif root.right and root.right.val == 1:
            #     return self.pruneTree(root.right)
            # else:
            #     return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        return root