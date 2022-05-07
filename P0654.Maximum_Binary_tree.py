# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        max_el = [i for i in range(len(nums)) if nums[i] == max(nums)]
        if len(max_el) > 0 and max_el[0] >= 0 and max_el[0] <= len(nums):
            left = self.constructMaximumBinaryTree(nums[0:max_el[0]])
            right = self.constructMaximumBinaryTree(nums[max_el[0]+1:])
            root = TreeNode(nums[max_el[0]])
            root.left = left
            root.right = right
        
            return root