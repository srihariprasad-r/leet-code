# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def dfs(n):
            if n == 1:
                return [TreeNode()]

            res = []
            for i in range(1, n, 2):
                j = n - 1 - i
                left = dfs(i)
                right = dfs(j)

                for l in left:
                    for r in right:
                        root = TreeNode()
                        root.left = l
                        root.right = r

                        res.append(root)
            return res
        return dfs(n)
