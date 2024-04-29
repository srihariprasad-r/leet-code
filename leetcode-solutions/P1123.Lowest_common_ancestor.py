# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def solution(node):
            if node is None:
                return node, 0

            leftNode, leftDepth = solution(node.left)
            rightNode, rightDepth = solution(node.right)

            if leftDepth == rightDepth:
                return node, leftDepth + 1
            elif leftDepth < rightDepth:
                return rightNode, rightDepth + 1
            else:
                return leftNode, leftDepth + 1

        return solution(root)[0]

# wrong submission
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def lca(node, parent, lvl):
            if not node: return parent, lvl

            if not node.left and not node.right:
                return parent, lvl

            pleft, leftlvl = lca(node.left, node, lvl+1)
            pright, rightlvl = lca(node.right, node, lvl+1)

            return pleft if leftlvl > rightlvl else pright , \
                leftlvl if leftlvl > rightlvl else rightlvl

        lparent, lvl1 =  lca(root.left, root, 1)
        rparent, lvl2 =  lca(root.right, root, 1)

        return lparent if lvl1 > lvl2 else rparent