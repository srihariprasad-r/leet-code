# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        
        def dfs(node):
            if node:
                dfs(node.left)
                result.append(node.val)
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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        ans = []
        stck = [root]

        el = stck[-1]

        while el:
            stck.append(el.left)
            el = el.left

        while stck:
            el = stck.pop()
            if el:
                ans.append(el.val)
            if el and el.right:
                el = el.right
                while el:
                    stck.append(el)
                    el = el.left

        return ans
