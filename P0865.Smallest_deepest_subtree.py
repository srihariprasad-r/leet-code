# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if not node:
                return 0, None
            
            height_left, left_node = dfs(node.left)
            height_right, right_node = dfs(node.right)
            
            if height_left == height_right:
                return height_left + 1, node
            elif height_left > height_right:
                return height_left + 1, left_node
            else:
                return height_right + 1, right_node
        
        return dfs(root)[1]