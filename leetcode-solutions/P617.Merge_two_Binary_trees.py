# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        elif t2 is None:
            return t1
        else:
            t1.val = t1.val + t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
    
# Method 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        root = None

        def dfs(node1, node2):
            if not node1 and not node2:
                return None
            elif not node2 and node1:
                return node1
            elif node2 and not node1:
                return node2

            s = 0
            if node1 and node2:
                s = node1.val + node2.val
            elif not node1 and node2:
                s = node2.val
            elif not node2 and node1:
                s = node1.val

            root = TreeNode(s)
            root.left = dfs(node1.left, node2.left)
            root.right = dfs(node1.right, node2.right)

            return root

        root = dfs(root1, root2)

        return root