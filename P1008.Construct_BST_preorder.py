# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = None
        
        def f(node, val):
            if node is None:
                return TreeNode(val)
            
            if val < node.val:
                node.left = f(node.left, val)
            else:
                node.right = f(node.right, val)
            
            return node
        
        for e in preorder:
            root = f(root, e)
        
        return root