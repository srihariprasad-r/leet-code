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