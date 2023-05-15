# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        heapq.heapify(res)

        def dfs(node, fl='s'):
            if not node:
                return

            dfs(node.left)
            if node:
                heapq.heappush(res, node.val)
            dfs(node.right)

            return res

        dfs(root1)
        dfs(root2)

        return heapq.nsmallest(len(res), res)