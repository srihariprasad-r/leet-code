# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        
        def dfs(node):
            if node:
                result.append(node.val)
                dfs(node.left)
                dfs(node.right)
            return result
        
        return dfs(root)


# Method 2
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        stck = [root]
        ans = []
        
        while stck:          
            el = stck.pop()
            ans.append(el.val)
            if el.right:
                stck.append(el.right)
            if el.left:
                stck.append(el.left)
        
        return ans
        