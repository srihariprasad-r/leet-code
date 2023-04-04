# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            left_node = self.maxDepth(root.left)
            right_node = self.maxDepth(root.right)            
        return max(left_node, right_node) + 1


# Method 2

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        self.res = float('-inf')

        def traverse(node):
            if not node:
                return 0
            self.depth += 1
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            self.res = max(self.res, self.depth)
            self.depth -= 1
            return self.res

        return traverse(root)
