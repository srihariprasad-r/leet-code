class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0

            if grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            return dfs(grid, i - 1, j) + \
                dfs(grid, i, j + 1) + \
                dfs(grid, i + 1, j) + \
                dfs(grid, i, j - 1) + 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt = dfs(grid, i, j)
                    res = max(res, cnt)

        return res