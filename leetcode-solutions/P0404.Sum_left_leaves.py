# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, dir=None):
            if node is None:
                return 0

            if not node.left and not node.right:
                return node.val if dir == 'left' else 0

            left_sum = helper(node.left, 'left')
            right_sum = helper(node.right, 'right')

            return left_sum + right_sum

        return helper(root, 0)

# Method 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, fl='root'):
            if not node:
                return 0

            if node.left:
                dfs(node.left, 'l')

            if node.right:
                dfs(node.right, 'r')

            if not node.left and not node.right and fl == 'l':
                self.ans += node.val

            return self.ans

        return dfs(root)

# wrong submission
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def f(node, s, sm):
            if not node:
                return sm

            if s == 'left': sm += node.val
            lsum = f(node.left, 'left', sm)
            rsum = f(node.right, 'right', 0)

            return lsum + rsum

        return f(root,'', 0)