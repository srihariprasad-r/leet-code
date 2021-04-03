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
        res = []
        from collections import deque
        
        q = deque()
        q.append(root)
        
        result.append([q[-1].val])
        
        while len(q) > 0:
            curList = []
            for _ in range(len(q)):
                curEl = q.popleft()
                if curEl.left:
                    q.append(curEl.left)
                    curList.append(curEl.left.val)
                if curEl.right:
                    q.append(curEl.right)
                    curList.append(curEl.right.val)
            if curList: result.append(curList)
        
        for i in range(len(result)):
            sum_level = sum(result[i])
            count_lvel = len(result[i])
            avg_level = float(sum_level)/float(count_lvel)
            res.append(avg_level)
        
        return res