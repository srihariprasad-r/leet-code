# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        mp = {}
        res = []

        def dfs(node, path=''):
            if not node:
                return ' '

            path += str(node.val)
            path += ' ' + dfs(node.left)
            path += ' ' + dfs(node.right)

            if path not in mp:
                mp[path] = 1
            else:
                mp[path] += 1
                if mp[path] == 2:
                    if node not in res:
                        res.append(node)

            return path

        dfs(root)
        return res