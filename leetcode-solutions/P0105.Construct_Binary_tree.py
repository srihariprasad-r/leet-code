# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid+1])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

# Method 2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def dfs(l, r):
            if l > r:
                return None
    
            value = preorder.pop(0)
            root = TreeNode(value)
            idx = inorder.index(value)
            root.left = dfs(l, idx-1)
            root.right = dfs(idx+1, r)
            
            return root
    
        return dfs(0, len(preorder)- 1)