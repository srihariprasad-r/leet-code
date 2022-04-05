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
