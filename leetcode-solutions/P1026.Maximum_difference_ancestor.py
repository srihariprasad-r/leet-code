# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, cur_min, cur_max):
            if not node:
                return cur_max - cur_min

            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)

            return max(dfs(node.left, cur_min, cur_max), dfs(node.right, cur_min, cur_max))

        return dfs(root, float('inf'), float('-inf'))

#wrong submission
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:    
        mxnode = root.val
        mnnode = root.val  
        def f(node, mxnode, mnnode):
            if not node: return mxnode, mnnode

            mxnode, mnnode = f(node.left, mxnode, mnnode)
            mxnode, mnnode = f(node.right, mxnode, mnnode)

            mxnode = max(node.val, mxnode)
            mnnode = min(node.val, mnnode)

            return mxnode , mnnode

        mxnode_left, mnnode_left = f(root.left, mxnode, mnnode)
        mxnode = root.val
        mnnode = root.val                  
        mxnode_right, mnnode_right = f(root.right, mxnode, mnnode)

        res  = abs(mxnode_left-mnnode_left) \
            if abs(mxnode_right-mnnode_right) < abs(mxnode_left-mnnode_left) \
            else abs(mxnode_right-mnnode_right)
        
        return  res