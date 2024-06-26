class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
                
        self.tempnode = root.left
        root.left = root.right
        root.right = self.tempnode
        
        self.invertTree(root.left)
        self.invertTree(root.right)        
        
        return root

# Method 2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root
        
# Method 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return

        self.invertTree(root.left)
        self.invertTree(root.right)

        tmp = root.left
        root.left = root.right
        root.right = tmp

        return root

# Method 4

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        node = None

        def dfs(node1):
            if not node1:
                return None

            node = TreeNode(node1.val)
            node.left = dfs(node1.right)
            node.right = dfs(node1.left)

            return node

        return dfs(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def f(node):
            if not node:
                return

            left = f(node.left)
            right = f(node.right)

            node.left, node.right =  node.right, node.left
            
            return node

        return f(root)