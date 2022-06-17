# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        s = []
        res = []
        ans = []
        res.append(root.val)
        s.append((root, res))

        while len(s) > 0:
            node, val = s.pop()
            if not node.left and not node.right:
                ans.append(val)
            if node.left:
                s.append((node.left, val + [node.left.val]))

            if node.right:
                s.append((node.right, val + [node.right.val]))

        return map(lambda x: str('->'.join(str(e) for e in x)), ans)
