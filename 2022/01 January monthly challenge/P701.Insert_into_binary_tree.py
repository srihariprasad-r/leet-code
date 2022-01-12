# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        
        def dfs(node, val):
            if val < node.val:
                if node.left:
                    return dfs(node.left, val)
                else:
                    node.left = TreeNode(val)
            else:
                if node.right:
                    return dfs(node.right, val)
                else:
                    node.right = TreeNode(val)
            
            return node
            
        dfs(root,val)
        return root
