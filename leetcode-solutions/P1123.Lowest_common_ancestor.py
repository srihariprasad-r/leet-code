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
        if root and not root.left and not root.right: return root

        mx = float('-inf')

        def lca(node, parent, lvl, mx):
            if not node: return None, 0

            if not node.left and not node.right:
                if mx == lvl:
                    return parent, lvl
                else:
                    return node, lvl
            elif not node.left or not node.right: 
                if mx == lvl: return node, lvl
            
            mx = max(mx, lvl+1)

            pleft, leftlvl = lca(node.left, node, lvl+1, mx)
            pright, rightlvl = lca(node.right, node, lvl+1, mx)

            return pleft if leftlvl > rightlvl else pright, \
                leftlvl if leftlvl > rightlvl else rightlvl

        lparent, lvl1 =  lca(root.left, root, 1, mx)
        rparent, lvl2 =  lca(root.right, root, 1, mx)
        # print(lparent, rparent)
        return lparent if lvl1 > lvl2 else rparent