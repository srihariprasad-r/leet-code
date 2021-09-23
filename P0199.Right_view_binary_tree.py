# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return
    
        res = {}
        
        def rightview(root, level):
            if root is None:
                return 
            
            if level not in res:
                res[level] = root.val
                
            rightview(root.right, level+1)
            rightview(root.left, level+1)
            
        rightview(root, 0) 
        
        return [v for v in res.values()]