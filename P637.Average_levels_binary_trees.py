from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """        
        result = []         
        queue = deque()

        queue.append(root)
        
        result.append(root.val)
        
        while len(queue)> 0:           
            output = 0
            cnt = 0                
            for _ in range(len(queue)):            
                curVal = queue.popleft()
                if curVal.left:
                    queue.append(curVal.left)                    
                    output += curVal.left.val
                    cnt += 1
                if curVal.right:
                    queue.append(curVal.right)
                    output += curVal.right.val
                    cnt += 1     
                
            if cnt > 0:  
                avg = float(output)/float(cnt)
                result.append(avg)                                     
                    
        return result