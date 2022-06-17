# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        new_dict = {}
        
        if root is None:
            return result
                
        def getNodes1(i, root1):
            if i == 0:
                new_dict.setdefault(i,[]).append(root.val)            
            if root1.left:
                new_dict.setdefault(i + 1,[]).append(root1.left.val)    
                getNodes1(i+1, root1.left)                                 
            if root1.right: 
                new_dict.setdefault(i + 1,[]).append(root1.right.val)                    
                getNodes1(i+1, root1.right)                                
        
        getNodes1(0, root)
        
        for k, v in new_dict.items():
            result.insert(k,v)
            
        return result[::-1]        