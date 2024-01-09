class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        t = 0
        cntfresh = 0
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j, 0))
                    visited[i][j] = 1
                if grid[i][j] == 1: cntfresh += 1

        while q:
            i, j, t = q.popleft()
            # tm = max(tm, t)
            direction = [(0, -1), (0, 1), (-1, 0), (1,0)]

            for d in direction:
                x = i + d[0]
                y = j + d[1]
                if x > -1 and y < len(grid[0]) and x < len(grid) and y > -1 and \
                    grid[x][y] == 1 and not visited[x][y]:
                    q.append((x, y, t+1))
                    visited[x][y] = 1
                    cnt += 1

        if cntfresh != cnt: return - 1

        return t