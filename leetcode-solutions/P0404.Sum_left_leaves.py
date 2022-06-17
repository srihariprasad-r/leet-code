# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, dir=None):
            if node is None:
                return 0

            if not node.left and not node.right:
                return node.val if dir == 'left' else 0

            left_sum = helper(node.left, 'left')
            right_sum = helper(node.right, 'right')

            return left_sum + right_sum

        return helper(root, 0)
