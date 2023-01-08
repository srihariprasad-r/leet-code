# wrong submission
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        pt = 0
        m = len(grid)
        n = len(grid[0])

        p = collections.deque()
        p.append((0, 0, grid[0][0]))
        grid[0][0] = 0

        d = [(0, 1), (1, 0)]

        while p:
            x, y, pts = p.popleft()

            if x == m - 1 and y == n - 1:
                break

            cur_x = x + d[0][0]
            cur_y = y + d[0][1]
            next_x = x + d[1][0]
            next_y = y + d[1][1]

            if ((0 <= cur_x < m and 0 < cur_y < n)
                    and (0 <= next_x < m and 0 <= next_y < n)):
                if grid[cur_x][cur_y] > grid[next_x][next_y]:
                    p.append((cur_x, cur_y, pts + grid[cur_x][cur_y]))
                    grid[cur_x][cur_y] = 0
                else:
                    p.append((next_x, next_y, pts + grid[next_x][next_y]))
                    grid[next_x][next_y] = 0
            else:
                if (0 <= cur_x < m and 0 < cur_y < n):
                    p.append((cur_x, cur_y, pts + grid[cur_x][cur_y]))
                    grid[cur_x][cur_y] = 0
                else:
                    p.append((next_x, next_y, pts + grid[next_x][next_y]))
                    grid[next_x][next_y] = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    pt += grid[i][j]

        return pt
