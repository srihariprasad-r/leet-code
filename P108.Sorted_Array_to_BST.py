# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
sys.setrecursionlimit(1500)

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0: return None
        return self.constructBST(nums, 0, len(nums)-1)
    
    def constructBST(self,nums, left, right):          
        if left > right: return None
        mid = (left+right)/2
        node = TreeNode(nums[mid])        
        node.left = self.constructBST(nums, left, mid-1)           
        node.right = self.constructBST(nums, mid +1 , right)                
        return node