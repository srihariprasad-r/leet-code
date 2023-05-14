# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        results = []
        def inorder(root):            
            if root:
                inorder(root.left)
                results.append(root.val)    
                inorder(root.right)
                
        inorder(root)
        
        tnode = ptr = TreeNode(0)
        
        for i in range(len(results)):
            ptr.right = TreeNode(results[i])
            ptr = ptr.right
            
        return tnode.right

# Method 2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(root):
            if root is None:
                return []
            
            return dfs(root.left) + [root.val] + dfs(root.right)
        
        ans = cur = TreeNode(-1)
        
        for c in dfs(root):
            cur.right = TreeNode(c)
            cur = cur.right
            
        return ans.right
            
# Method 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        n = self.node = TreeNode()

        def dfs(node1):
            if not node1:
                return None

            dfs(node1.left)
            self.node.right = TreeNode(node1.val)
            self.node = self.node.right
            dfs(node1.right)

            # return self.node

        dfs(root)

        return n.right
