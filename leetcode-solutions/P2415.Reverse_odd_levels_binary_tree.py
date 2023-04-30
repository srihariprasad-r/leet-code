# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node1, node2, lvl):
            if node1 is None or node2 is None:
                return

            invert(node1.left, node2.right, lvl+1)
            invert(node1.right, node2.left, lvl+1)

            if lvl % 2 == 0:
                node1.val, node2.val = node2.val, node1.val

        invert(root.left, root.right, 0)

        return root