# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        if root is None:
            return None
        
        node = root
        
        count, level = 0, 0
        
        def depth(node):
            if node is None:
                return 0
            else:
                left_node = depth(node.left)
                right_node = depth(node.right)
        
            return max(left_node, right_node) + 1
              
        count = depth(root)        

        def dfs(node, level):
            if node.left is None and node.right is None and level ==  count:
                return [node.val]
            elif node.left is not None and node.right is not None:                             
                return dfs(node.left, level + 1) + dfs(node.right, level + 1)
            elif node.left is not None:        
                return dfs(node.left, level + 1)
            elif node.right is not None:        
                return dfs(node.right, level + 1)
            else:
                return []
            
        return sum(dfs(root, level + 1))                

# Method 2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dct = {}

        q = deque()
        q.append((root, 0))

        while len(q) > 0:
            el, lvl = q.popleft()

            dct.setdefault(lvl, []).append(el.val)

            if el.left:
                q.append((el.left, lvl + 1))

            if el.right:
                q.append((el.right, lvl + 1))

        return sum(dct[max(dct.keys())])

# Method 3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dct = defaultdict(int)

        def dfs(node, lvl):
            if not node:
                return

            dct[lvl] += node.val
            dfs(node.left, lvl+1)
            dfs(node.right, lvl+1)

            return dct[max(dct.keys())]

        return dfs(root, 0)