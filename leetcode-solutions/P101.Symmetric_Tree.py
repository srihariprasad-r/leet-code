# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSymmentric(root.left, root.right)
    
    def isSymmentric(self,left, right):
        if ((left is None) or (right is None)):
            return left == right
        
        if left.val != right.val:
            return False
        
        return self.isSymmentric(left.left, right.right) and self.isSymmentric(left.right, right.left)
    
# Method 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if not node1 or not node2:
                return node1 == node2

            n1 = node1.left.val if node1.left else 0
            n2 = node2.right.val if node2.right else 0

            n3 = node2.left.val if node2.left else 0
            n4 = node1.right.val if node1.right else 0

            return node1.val == node2.val and \
                n1 == n2 and \
                n3 == n4 and \
                dfs(node1.left, node2.right) and \
                dfs(node1.right, node2.left)

        return dfs(root, root)
            
