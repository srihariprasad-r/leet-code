# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return
    
        res = {}
        
        def rightview(root, level):
            if root is None:
                return 
            
            if level not in res:
                res[level] = root.val
                
            rightview(root.right, level+1)
            rightview(root.left, level+1)
            
        rightview(root, 0) 
        
        return [v for v in res.values()]

# Method 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        q = deque()
        res = []
        st = set()

        q.append((root,0))

        while q:            
            node, lvl = q.popleft()   

            if node:  
                if lvl not in st:                               
                    res.append(node.val)                
                    st.add(lvl)              
    
            if node.right: 
                q.append((node.right, lvl+1))                
            if node.left:
                q.append((node.left, lvl+1))                              
        
        return res