# Definition for a binary tree node.

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):            
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        
        if root is None:
            return result    
        
        queue = deque()
        
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
                maxVal = max(curList)
            result.append(maxVal)
        
        return result