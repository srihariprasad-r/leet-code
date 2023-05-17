# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        stck = []
        self.s = 0
        stck.append((root, None, None))

        while stck:
            for _ in range(len(stck)):
                node, p, g = stck.pop()

                if g and g.val % 2 == 0:
                    self.s += node.val if node else 0

                if node.left:
                    stck.append((node.left, node, p))

                if node.right:
                    stck.append((node.right, node, p))

        return self.s