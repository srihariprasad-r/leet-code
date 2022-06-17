# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        tmpleft = root.left
        tmpright = root.right

        root.left = None

        self.flatten(tmpleft)
        self.flatten(tmpright)

        root.right = tmpleft

        cur = root
        while cur.right:
            cur = cur.right

        cur.right = tmpright