# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.res = collections.defaultdict(int)

        def ssum(node):
            if not node:
                return 0

            l = ssum(node.left) if node.left else 0
            r = ssum(node.right) if node.right else 0

            s = node.val + l + r

            if not(s in self.res):
                self.res[s] = 1
            else:
                self.res[s] += 1

            return s

        ssum(root)
        mx_v = float('-inf')
        for k, v in self.res.items():
            if v > mx_v:
                r = v
                mx_v = v

        o = []
        for k, v in self.res.items():
            if v == r:
                o.append(k)

        return o