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

# Method 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(nums,l, r):
            if l > r: return None
            if l == r: return TreeNode(nums[l])
            mid = l + (r-l)//2
            root = TreeNode(nums[mid])
            root.left = dfs(nums, l, mid-1)
            root.right = dfs(nums, mid + 1, r)

            return root

        return dfs(nums, 0, len(nums)-1)