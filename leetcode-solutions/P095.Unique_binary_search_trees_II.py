# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.somemethod(1, n)
    
    def somemethod(self, s, e):
        lst = []
        if s > e:
            lst.append(None)
            return lst
        
        if s == e:
            lst.append(TreeNode(s))
            return lst
        
        for i in range(s, e+1):
            lefttree = self.somemethod(s, i-1)
            righttree = self.somemethod(i+1, e)
            
            for l in lefttree:
                for r in righttree:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    lst.append(node)
                    
        return lst

# Method 2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def dfs(nums):
            if not nums:
                return [None]

            ans = []

            for i in range(len(nums)):
                left = dfs(nums[:i])
                right = dfs(nums[i+1:])

                for l in left:
                    for r in right:
                        root = TreeNode(nums[i])
                        root.left = l
                        root.right = r
                        ans.append(root)

            return ans

        nums = [i for i in range(1, n+1)]

        return dfs(nums)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        @lru_cache(None)
        def dfs(left, right):
            if left > right:
                return [None]
            if left == right:
                return [TreeNode(left)]
            ans = []
            for root in range(left, right+1):
                left_nodes = dfs(left, root-1)
                right_nodes = dfs(root+1, right)
                for l in left_nodes:
                    for r in right_nodes:
                        ans.append(TreeNode(root, l, r))

            return ans

        return dfs(1, n)
