# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dct = {}

        def helper(node):
            if not node:
                return 0

            if node in self.dct:
                return self.dct[node]

            left_sum = right_sum = 0

            if node.left:
                left_sum = helper(node.left.left) + helper(node.left.right)

            if node.right:
                right_sum = helper(node.right.left) + helper(node.right.right)

            current = node.val + left_sum + right_sum
            not_current = helper(node.left) + helper(node.right)

            self.dct[node] = max(current, not_current)
            return self.dct[node]

        return helper(root)
