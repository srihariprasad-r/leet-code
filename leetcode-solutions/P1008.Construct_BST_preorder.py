# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = None
        
        def f(node, val):
            if node is None:
                return TreeNode(val)
            
            if val < node.val:
                node.left = f(node.left, val)
            else:
                node.right = f(node.right, val)
            
            return node
        
        for e in preorder:
            root = f(root, e)
        
        return root

# Method 2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        def f(lst, n, pos, node, left_range, right_range):
            if pos == n or lst[pos] < left_range or lst[pos] > right_range:
                return pos

            if lst[pos] < node.val:
                node.left = TreeNode(lst[pos])
                pos += 1
                pos = f(lst, n, pos, node.left, left_range, node.val - 1)

            if pos == n or lst[pos] < left_range or lst[pos] > right_range:
                return pos

            node.right = TreeNode(lst[pos])
            pos += 1
            pos = f(lst, n, pos, node.right, node.val + 1, right_range)

            return pos

        if len(preorder) == 0:
            return None

        n = len(preorder)
        root = TreeNode(preorder[0])

        if n == 1:
            return root

        f(preorder, n, 1, root, float('-inf'), float('inf'))

        return root