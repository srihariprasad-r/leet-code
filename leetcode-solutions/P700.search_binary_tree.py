# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        if root.val == val:
            return root
        elif root.left and root.val > val:
            return self.searchBST(root.left, val)
        elif root.right and root.val < val:            
            return  self.searchBST(root.right, val)

              
        return None                  