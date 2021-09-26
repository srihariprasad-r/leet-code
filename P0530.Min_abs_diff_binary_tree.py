# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return
        res = set()
        final_min = float('inf')
        
        def absdiff(arr):
            arr = list(arr)
            diff = float('inf')
            for i in range(len(arr)):
                for j in range(i+1, len(arr)):
                    if abs(arr[i] - arr[j]) <= diff:
                        diff = abs(arr[i] - arr[j])
            return diff
            
            
        def dfs(node, minval, res):
            if not node:
                res.add(minval)
                return minval
            
            left = dfs(node.left, min(minval, abs(node.val - node.left.val if node.left 
                                                  else float('inf')) if node 
                                      else float('inf')), res
                      )

            right = dfs(node.right, min(minval, abs(node.val - node.right.val if node.right 
                                                    else float('inf')) if node 
                                        else float('inf')), res
                       )
            return res
        
        res = dfs(root, float('inf'), res)
    
        return absdiff(res) if len(res) > 2 else min(res)