# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        graph = defaultdict(list)
        
        queue = deque([root])
        
        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                
            if node.right:
                queue.append(node.right)
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
        
        queue = deque([(target.val,0)])
        visited = set()
        res = []
        cnt = 0
        
        while queue:
            node, level = queue.popleft()
            visited.add(node)
            if level == k:
                res.append(node)
            
            for neighbour in range(len(graph[node])):
                if graph[node][neighbour] not in visited:
                    queue.append((graph[node][neighbour], level + 1))
                    visited.add(graph[node][neighbour])
            
            cnt += 1
        
        return res