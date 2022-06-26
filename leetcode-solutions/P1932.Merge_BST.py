# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def canMerge(self, trees):
        """
        :type trees: List[TreeNode]
        :rtype: TreeNode
        """
        leaves = set()
        tree_dict = {}
        
        for tree in trees:
            tree_dict[tree.val] = tree
            if tree.left:
                leaves.add(tree.left.val)
            
            if tree.right:
                leaves.add(tree.right.val)
                
        root = None
        for tree in trees:
            if tree.val not in leaves:
                root = tree
                break
                
        if not root:
            return None
        
        curLeaves = {}
        if root.left:
            curLeaves[root.left.val] = (-sys.maxsize, root.val, root, 0)
        
        if root.right:
            curLeaves[root.right.val] = (root.val, sys.maxsize, root, 1)
            
        del tree_dict[root.val]
        
        while tree_dict:
            findTree = False
            for leaf, (low, high, parent, leftOrRight) in curLeaves.items():
                if leaf in tree_dict:
                    childTree = tree_dict[leaf]
                    del curLeaves[leaf]
                    
                    if childTree.left:
                        if low < childTree.left.val < high \
                            and childTree.left.val not in curLeaves:
                            curLeaves[childTree.left.val] = (low, childTree.val, \
                                                            childTree, 0)
                        else:
                            return None
                        
                    if childTree.right:
                        if low < childTree.right.val < high \
                            and childTree.right.val not in curLeaves:
                            curLeaves[childTree.right.val] = (childTree.val, \
                                                              high, childTree, 1)
                        else:
                            return None
                        
                    if leftOrRight == 0:
                        parent.left = childTree
                    else:
                        parent.right = childTree
                        
                    findTree = True
                    del tree_dict[childTree.val]
                    
            if not findTree:
                return None
            
        return root