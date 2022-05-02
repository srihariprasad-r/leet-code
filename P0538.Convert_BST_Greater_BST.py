# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.global_value = 0

        def helper(node):
            if not node:
                return None

            helper(node.right)
            node.val += self.global_value
            self.global_value = node.val
            helper(node.left)

            return node

        return helper(root)
