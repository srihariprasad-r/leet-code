# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        lvl = {}
        lst = [-float('inf')]
        q = []
        q.append((root, 1))

        while len(q) > 0:
            el, level = q.pop(0)
            lvl.setdefault(level, []).append(el.val)

            if el.left:
                q.append((el.left, level+1))

            if el.right:
                q.append((el.right, level+1))

        for k, v in lvl.items():
            lst.insert(k, sum(v))

        max_el = max(lst)
        for i in range(len(lst)):
            if lst[i] == max_el:
                return i