class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        ans = [[0]* n for _ in range(m)]
        dist = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i, j))
                    
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if mat[i][j] == 1:
                    ans[i][j] = dist
                    
                for d in directions:
                    dx = i + d[0]
                    dy = j + d[1]
                    
                    if 0 <= dx < m and 0 <= dy < n and (dx, dy) not in visited:
                        queue.append((dx, dy))
                        visited.add((dx, dy))
                        
            dist += 1
        
        return ans