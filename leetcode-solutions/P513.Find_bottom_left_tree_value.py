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

# wrong submission

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(node, st, lvl):
            if not node:
                return None

            if not node.right and not node.left:
                if st == 'l':
                    heapq.heappush(res, (-lvl, node.val))
                elif st == 'root':
                    heapq.heappush(res, (0, node.val))
                return

            dfs(node.left, 'l', lvl+1)
            dfs(node.right, 'r', lvl+1)

        dfs(root, 'root', 0)

        if res:
            o = heapq.heappop(res)
            return o[1]
        
# wrong submission
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root and not root.left and not root.right: return root.val

        def leftmost(node, flag, lvl):
            if not node: 
                return 99999, -1

            if not node.left and not node.right:
                return node.val, lvl

            rightnode, rightlvl = leftmost(node.right, 'right', lvl+1)
            leftnode, leftlvl = leftmost(node.left, 'left', lvl+1)            

            return leftnode if leftlvl > rightlvl else rightnode, \
                leftlvl if leftlvl > rightlvl else rightlvl

        leftnode, leftlvl  = leftmost(root.left, '', 1)
        rightnode, rightlvl = leftmost(root.right, '', 1)

        if leftlvl == rightlvl:
            if leftnode != 99999:
                return leftnode
            else:
                return rightnode
        elif rightlvl > leftlvl:
            if rightnode != 99999:
                return rightnode
            else:
                return leftnode

        return leftnode if leftlvl > rightlvl else rightnode