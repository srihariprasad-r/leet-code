# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if (root.val == 1) or (root.val == 0 and (root.left or root.right)):
            return root
        else:
            return None

# wrong submission
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        rN = None
        def prune(node):
            if not node: return

            rN = None
            if node.val != 1 and not node.left and not node.right:
                return rN

            rN = TreeNode(node.val)
            rN.left = prune(node.left)
            if rN.left and rN.left.val != 1 and not node.left and not node.right:
                return rN 
            rN.right = prune(node.right)
            if rN.right and rN.right.val != 1 and not node.left and not node.right:
                return rN   

            return rN

        rN = prune(root)          
        return prune(rN)    