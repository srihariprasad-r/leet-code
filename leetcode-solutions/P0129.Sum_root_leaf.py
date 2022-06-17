# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []

        def helper(node, val):
            if node is None:
                return 0

            val = val * 10 + node.val
            if not node.left and not node.right:
                return val

            return helper(node.left, val) + helper(node.right, val)

        return helper(root, 0)
