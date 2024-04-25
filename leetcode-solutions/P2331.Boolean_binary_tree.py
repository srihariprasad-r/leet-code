# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def f(node):
            if not node: return True

            if not(node.val in (2, 3)): 
                return True if node.val == 1 else False

            lval = 0
            rval = 0

            lval = f(node.left)
            rval = f(node.right)

            if node.val == 2:
                return lval | rval
            else:
                return lval & rval

        return f(root)