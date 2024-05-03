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

# Method 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(nums):
            if not nums: return

            mx = max(nums)
            i = nums.index(mx)
            root = TreeNode(nums[i])
            root.left = dfs(nums[:i])
            root.right = dfs(nums[i+1:])

            return root

        return dfs(nums)
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        rN = None
        
        def f(lst):
            if not lst: return None
            mx = max(lst)
            rN = TreeNode(mx)
            idx = lst.index(mx)
            rN.left = f(lst[:idx])
            rN.right = f(lst[idx+1:])

            return rN

        return f(nums)