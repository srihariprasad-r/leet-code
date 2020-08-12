# Definition for a binary tree node.
 from collections import deque
 
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """               
        result = [[]]

        queue = deque()
        
        if root is None:
            return result[1:]

        queue.append(root)
        
        while len(queue)> 0:
            curList = []
            for _ in range(len(queue)):
                curVal = queue.popleft()
                curList.append(curVal.val)              
                if curVal.left:
                    queue.append(curVal.left)
                if curVal.right:
                    queue.append(curVal.right)
            result.append(curList)  
        
        return result[1:]
        