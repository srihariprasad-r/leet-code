# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        
        queue = deque()
        
        result = []
        
        if root is None:
            return result
        
        queue.append(root)
        
        while len(queue) > 0:
            curList = []
            for _ in range(len(queue)):
                curVal = queue.popleft()
                if curVal.left:
                    queue.append(curVal.left)                    
                if curVal.right:
                    queue.append(curVal.right)                    
                
                curList.append(curVal.val)
                                
            result.append(curList)
        
        for i in range(len(result)):
            if i % 2 == 1:
                result[i] = result[i][::-1]
        
        return result