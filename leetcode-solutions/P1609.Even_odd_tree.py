# wrong submission

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def increasing(arr):
            if not arr:
                return False

            if len(arr) == 1:
                return True

            if arr[0] < arr[-1]:
                return True

            return False

        stck = []
        lvl_all = collections.defaultdict(list)
        stck.append((root, 0))

        while stck:
            for _ in range(len(stck)):
                node, lvl = stck.pop()

                if lvl % 2:
                    if node.val % 2:
                        return False
                else:
                    if not node.val % 2:
                        return False

                if node.left:
                    stck.append((node.left, lvl+1))

                if node.right:
                    stck.append((node.right, lvl+1))

                if lvl > 0:
                    lvl_all[lvl].append(node.val)

        fl = True

        for k, v in lvl_all.items():
            if len(set(v)) != len(v):
                return False
            if k % 2 == 0:
                if not increasing(v[::-1]):
                    fl = False
            else:
                if increasing(v[::-1]):
                    fl = False

        return fl