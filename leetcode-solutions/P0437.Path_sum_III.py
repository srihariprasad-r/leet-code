# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        self.result = 0
        self.sum_cnt = defaultdict(int)
        self.sum_cnt[0] = 1

        if not root:
            return self.result

        def dfs(node, running_sum):
            if not node:
                return

            running_sum += node.val

            if (running_sum - targetSum) in self.sum_cnt:
                self.result += self.sum_cnt[running_sum - targetSum]

            self.sum_cnt[running_sum] += 1

            dfs(node.left, running_sum)
            dfs(node.right, running_sum)
            # backtrack to remove sum collected
            self.sum_cnt[running_sum] -= 1

            return self.result

        return dfs(root, 0)

# wrong submission
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:   
        if not root: return 0
        self.cnt = 0
        self.dct = collections.defaultdict(int)
        self.dct[0] = 1
        self.dct[root.val] = 1
        cnt = 0     
        def f(node, s):
            if not node: return

            self.dct[node.val] += 1

            if s + node.val - targetSum in self.dct: 
                self.cnt += self.dct[s + node.val - targetSum]    

            self.dct[s+node.val] += 1
            f(node.left, s + node.val)             
            f(node.right, s + node.val)
            self.dct[node.val] -= 1

        f(root.left, root.val) 
        f(root.right, root.val) 

        return self.cnt