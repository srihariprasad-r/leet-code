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