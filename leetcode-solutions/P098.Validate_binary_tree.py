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