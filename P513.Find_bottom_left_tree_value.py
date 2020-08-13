# Definition for a binary tree node.

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        result = []         
        queue = deque()
        
        queue.append(root)
        
        while len(queue)> 0:
            curList = []
            for _ in range(len(queue)):
                curVal = queue.popleft()
                if curVal.left:
                    queue.append(curVal.left)
                    curList.append(curVal.left.val)
                if curVal.right:
                    queue.append(curVal.right)
                    
                if curVal.left is None:
                    curList.append(curVal.val)
        
            if len(curList) > 0:
                del result[:]
                result.append(curList)
        
        return result[0][0]
