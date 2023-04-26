# wrong submission

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 0
        def dfs(grid, i, j):
            m = len(grid)
            n = len(grid[0])
            q = deque()
            steps = 0
            dirs = [(-1,0), (1, 0), (0, 1), (0, -1)]
            q.append((i, j))

            while q:
                t = len(q)
                steps += 1
                for i in range(t):
                    c = q.popleft()
                    for d in dirs:
                        new_x, new_y = c[0] + d[0], c[1] + d[1]
                        if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n:
                            if grid[c[0]][c[1]] >= grid[new_x][new_y]: 
                                continue
                            c = tuple([new_x, new_y])
                            q.append(c)
                # steps += 1

            return steps

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res =  max(res, dfs(matrix, i, j))

        return res

# Method 2


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(matrix)
        n = len(matrix[0])
        dp = {}

        def dfs(grid, i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            res = 1
            for d in dirs:
                new_x, new_y = d[0] + i, d[1] + j
                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] > grid[i][j]:
                    res = max(res, 1 + dfs(grid, new_x, new_y))
            dp[(i, j)] = res
            return res

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dfs(matrix, i, j))

        return res