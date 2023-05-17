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

            if arr[0] < arr[-1]:
                return False

            return True

        stck = []
        lvl_all = collections.defaultdict(list)
        stck.append((root, 0))

        while stck:
            for _ in range(len(stck)):
                node, lvl = stck.pop()

                if node.left:
                    stck.append((node.left, lvl+1))

                if node.right:
                    stck.append((node.right, lvl+1))

                lvl_all[lvl].append(node.val)

        fl = True
        for k, v in lvl_all.items():
            if not(k % 2 == 0 and increasing(v)):
                fl = False
            elif not(k % 2 and not increasing(v)):
                fl = False

        return fl