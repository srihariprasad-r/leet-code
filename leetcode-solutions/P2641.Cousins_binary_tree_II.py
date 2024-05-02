# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        import collections
        def f(node, parent, lvl):
            if not node:
                return 0

            s[lvl] += node.val
            f(node.left, node, lvl+1) 
            f(node.right, node, lvl+1)
            
        s = collections.defaultdict(int)
        f(root, root, 0)

        def f1(node, lvl, new):
            v = s[lvl+1] - ((node.left.val if node.left else 0) + (node.right.val if node.right else 0))
 
            if node.left:
                new.left = TreeNode(v)
                f1(node.left, lvl+1, new.left)
            if node.right:
                new.right = TreeNode(v)
                f1(node.right, lvl+1, new.right)                

            return new

        return f1(root, 0, TreeNode(0))