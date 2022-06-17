# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s = []
        ans = []
        res = [root.val]
        s.append((root, res))

        while len(s) > 0:
            node, res = s.pop()
            if not node.left and not node.right:
                ans.append(res)
            if node.left:
                s.append((node.left, res + [node.left.val]))
            if node.right:
                s.append((node.right, res + [node.right.val]))

        return sum(map(lambda x: int(''.join(str(e) for e in x), 2), ans))
