# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node, subnode):
            if node is None or subnode is None:
                return node == subnode

            return node.val == subnode.val and \
                dfs(node.left, subnode.left) and dfs(node.right, subnode.right)

        def checkTree(node):
            if not node:
                return False

            if dfs(node, subRoot):
                return True

            return checkTree(node.left) or checkTree(node.right)

        return checkTree(root)
    
# wrong submission
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(node1, node2):
            if not node1 and not node2: return True

            if not node1 or not node2: return False

            return node1.val == node2.val and compare(node1.left, node2.left) \
                and compare(node1.right, node2.right)

        def f(node1, node2):
            if not node1 or not node2: return False

            if node1.val == node2.val:
                return compare(node1, node2)

            left = False
            right = False
            left = f(node1.left, node2)
            right = f(node1.right, node2)

            return left or right

        return f(root, subRoot)