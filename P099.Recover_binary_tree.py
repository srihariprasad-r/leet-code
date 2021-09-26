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
