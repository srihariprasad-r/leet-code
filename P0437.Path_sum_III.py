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
