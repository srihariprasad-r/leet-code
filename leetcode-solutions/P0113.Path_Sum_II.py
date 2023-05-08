# wrong submission

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, s, tmp=[]):
            if not node:
                if s == targetSum:
                    if tmp not in res:
                        res.append(copy.deepcopy(tmp))
                return

            if s > targetSum:
                return

            s += node.val
            if s == targetSum:
                if not node.left and not node.right:
                    if tmp not in res:
                        res.append(copy.deepcopy(tmp + [node.val]))
                return res
            else:
                dfs(node.left, s, tmp + [node.val])
                dfs(node.right, s, tmp + [node.val])

            return res

        return dfs(root, 0, [])