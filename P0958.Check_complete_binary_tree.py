# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = deque()
        
        queue.append(([root,1]))
        
        mlen = 0
        arr = []
        
        while queue:
            qlen = len(queue)
            for i in range(qlen):
                arr.append(queue[i][1])
                
            for _ in range(len(queue)):
                node, idx = queue.popleft()
                
                if node.left:
                    queue.append((node.left, idx*2))
                
                if node.right:
                    queue.append((node.right, idx*2+1))
        
        return False if max(arr) != len(arr) else True