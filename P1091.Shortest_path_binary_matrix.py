class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] or grid[m-1][n-1]:
            return -1

        directions = [[0, -1], [0, 1], [-1, -1],
                      [-1, 0], [-1, 1], [1, -1], [1, 0], [1, 1]]
        visited = [[False for _ in range(n+1)] for _ in range(m+1)]

        q = deque()
        q.append(((0, 0), 1))

        visited[0][0] = True

        while len(q) > 0:
            coordinates, distance = q.popleft()
            x, y = coordinates[0], coordinates[1]

            if x == m - 1 and y == n - 1:
                return distance

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n \
                        and grid[new_x][new_y] == 0 and not visited[new_x][new_y]:
                    q.append(((new_x, new_y), distance + 1))
                    visited[new_x][new_y] = True
                    # cnt += 1

        return -1