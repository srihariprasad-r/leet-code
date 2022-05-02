# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.sum = 0
        
        def helper(node, left, right):
            if node is None:
                return
            
            if node.val >= left and node.val <= right:
                self.sum += node.val
                helper(node.left, left, node.val)
                helper(node.right, node.val, right)
            elif node.val < left:
                helper(node.right, left, right)
            elif node.val > right:
                helper(node.left, left, right)
                
            return self.sum
        
        return helper(root, low, high)