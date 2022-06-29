# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return

        s = []
        s.append((root, -float('inf'), float('inf')))

        while len(s) > 0:
            el, left, right = s.pop()
            if el:
                if el.val <= left or right <= el.val:
                    return False
            if el.left:
                s.append((el.left, left, el.val))

            if el.right:
                s.append((el.right, el.val, right))

        return True


# Method 2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root, left, right):
            if not root:
                return True
            
            if root.val >= left and root.val <= right:
                return dfs(root.left, left, root.val - 1) \
                    and dfs(root.right, root.val + 1, right)
            
            return False
        
        return dfs(root, float('-inf'), float('inf'))