# Wrong submission

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = []
        q.append((root, root.val, 0))
        lvl = {}
        while len(q) > 0:
            el, val, level = q.pop(0)
            lvl.setdefault(level,[]).append(val)
            if el.left:
                q.append((el.left, el.left.val, level + 1))
            if el.right:
                q.append((el.right, el.right.val, level + 1))
                    
        def all_even(arr):
            return all(not arr[i]%2 for i in range(len(arr)))
        
        def all_odd(arr):
            return all(arr[i]%2 for i in range(len(arr)))
        
        def strictly_increasing(arr): 
            return all(arr[i] < arr[i+1] for i in range(len(arr)-1))
        
        def strictly_decreasing(arr): 
            return all(arr[i] > arr[i+1] for i in range(len(arr)-1))
        
        for k, v in lvl.items():
            if k % 2:
                if not strictly_decreasing(v) or not all_even(v):
                    return False
                else:
                    continue
            else:
                # even
                if len(v) == 1: continue
                if not strictly_increasing(v) or not all_odd(v):
                    return False
                else:
                    continue
                        
        return True