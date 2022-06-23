class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        queue = deque()
        queue.append((0, 0, k))
        seen = set()
        seen.add((0, 0, k))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = 0
        
        while queue:
            for _ in range(len(queue)):
                cur_x, cur_y, cur_k = queue.popleft()
                
                if cur_x == m - 1 and cur_y == n- 1:
                    return res
                
                for d in directions:
                    new_x = cur_x + d[0]
                    new_y = cur_y + d[1]
                    
                    if 0 <= new_x < m and 0 <= new_y < n:
                        if grid[new_x][new_y]:
                            if cur_k > 0 and (new_x, new_y, cur_k - 1)  not in seen:
                                queue.append((new_x, new_y, cur_k - 1))
                                seen.add((new_x, new_y, cur_k - 1))
                        else:
                            if (new_x, new_y, cur_k)  not in seen:
                                queue.append((new_x, new_y, cur_k))
                                seen.add((new_x, new_y, cur_k))
                                
            res += 1
                                
        return -1