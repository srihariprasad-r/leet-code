# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        def inorder(root, res):
            if root.left:
                inorder(root.left, res)
            res.append(root)
            if root.right:
                inorder(root.right, res)
            return res

        arr = inorder(root, res=[])

        first = second = None

        for i in range(len(arr)-1):
            if arr[i] and arr[i+1]:
                if arr[i].val > arr[i+1].val:
                    if not first:
                        first = arr[i]
                    second = arr[i+1]

        first.val, second.val = second.val, first.val

        return arr

# Method 2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.first = self.pre = self.second = None
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            if self.pre and node.val < self.pre.val:
                self.first = node
                
                if not self.second:
                    self.second = self.pre
                else:
                    return

            self.pre =  node

            inorder(node.right)
            
        inorder(root)

        self.first.val, self.second.val = self.second.val, self.first.val

# almost same as above

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.frst = None
        self.scnd = None
        self.prv = None

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            if self.prv and not self.frst and node.val <= self.prv.val:
                self.frst = self.prv

            if self.frst and node.val <= self.prv.val:
                self.scnd = node
            self.prv = node
            dfs(node.right)

        dfs(root)
        self.frst.val, self.scnd.val = self.scnd.val, self.frst.val
