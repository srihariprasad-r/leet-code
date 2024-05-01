# wrong submission
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def f(node, c):
            if not node:
                return ''

            l = ''
            r = ''
            c = str(node.val)
            l = '(' + str(f(node.left, c )) + ')'
            if node.right: r = '(' + f(node.right, c) + ')'
            r = r.replace('()','')

            return (c + l + r)

        return f(root, '')