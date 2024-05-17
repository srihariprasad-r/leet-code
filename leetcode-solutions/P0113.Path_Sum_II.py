# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        if not root:
            return []

        def dfs(node, s, ans):
            if not node:
                return 0

            if not node.left and not node.right:
                s -= node.val
                if s == 0:
                    res.append(copy.deepcopy(ans + [node.val]))
                    return
            # commented due to -ve values passed as input
            #     elif s < 0:
            #         return

            # if s < 0:
            #     return

            ans.append(node.val)
            s -= node.val
            dfs(node.left, s, ans)
            dfs(node.right, s, ans)
            ans.pop()

            return

        dfs(root, targetSum, [])

        return res
    
# wrong submission
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        
        if root and not root.left and not root.right:
            if root.val == targetSum: return [[root.val]]
            
        res = []
        def f(node, l):
            if not node: return
            if node and not node.left and not node.right:
                if l and sum(l) + node.val == targetSum: 
                    l.append(node.val)
                    res.append(copy.deepcopy(l))
                return
            
            l.append(node.val)
            f(node.left, l)
            f(node.right, l)
            l.pop()

            return res

        f(root.left, [root.val])
        f(root.right, [root.val])

        return res