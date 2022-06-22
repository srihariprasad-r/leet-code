class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = collections.deque()
        seen = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    seen.add((i, j))
                    
                    while queue:
                        cur_x, cur_y = queue.popleft()
                        
                        for d in directions:
                            new_x = cur_x + d[0]
                            new_y = cur_y + d[1]
                            
                            if 0 <= new_x < m and 0 <= new_y < n \
                                and grid[new_x][new_y] == 1 and (new_x, new_y) not in seen:
                                queue.append((new_x, new_y))
                                seen.add((new_x, new_y))

                    queue = deque(seen)
                    distance = 0

                    while queue:
                        for _ in range(len(queue)):
                            cur_x, cur_y = queue.popleft()

                            if grid[cur_x][cur_y] == 1 and distance > 0:
                                return distance - 1

                            for d in directions:
                                new_x = cur_x + d[0]
                                new_y = cur_y + d[1]

                                if 0 <= new_x < m and 0 <= new_y < n \
                                    and not((new_x, new_y) in seen):
                                        queue.append((new_x, new_y))
                                        seen.add((new_x, new_y))

                        distance += 1
                                