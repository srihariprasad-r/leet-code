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
        lst = []

        def dfs(node, tmp=''):
            if not(node.left) and not(node.right):
                tmp += str(node.val)
                lst.append(tmp)
                tmp = ''
                return

            if node.left:
                dfs(node.left, tmp + str(node.val))
            if node.right:
                tmp = dfs(node.right, tmp + str(node.val))

        dfs(root)
        return sum(map(lambda x: int(x, 2), lst))
