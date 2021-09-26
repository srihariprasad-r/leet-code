# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return

        def dfs(root, res=[]):
            if root.left:
                dfs(root.left, res)
            if root.right:
                dfs(root.right, res)
            res.append(root.val)
            return res

        return dfs(root)