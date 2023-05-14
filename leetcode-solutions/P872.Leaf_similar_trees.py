# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):    
    def leafValue(self,root):
        if root.left is None and root.right is None:
            return [root.val]
        elif root.left is not None and root.right is not None:
            return self.leafValue(root.left) + self.leafValue(root.right)
        elif root.left is not None:
            return self.leafValue(root.left)
        elif root.right is not None:
            return self.leafValue(root.right)
    
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.leafValue(root1) == self.leafValue(root2)

# Method 2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def helper(node):
            q = deque()
            q.append(node)

            ans = []

            while len(q) > 0:
                el = q.pop()
                if not el.left and not el.right:
                    ans.append(el.val)

                if el.left:
                    q.append(el.left)

                if el.right:
                    q.append(el.right)

            return ans
        return helper(root1) == helper(root2)

# Method 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        n1 = list()
        n2 = list()

        def dfs(node1, fl='s'):
            if not node1:
                return None

            if not node1.left and not node1.right:
                if fl != 's':
                    n1.append(node1.val)
                else:
                    n2.append(node1.val)
                return

            dfs(node1.left, fl)
            dfs(node1.right, fl)

            return

        dfs(root1, fl='f')
        dfs(root2)

        return n1 == n2
