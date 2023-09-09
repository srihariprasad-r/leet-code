class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        res = 0

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return

            if grid[i][j] == 0:
                return

            grid[i][j] = 0
            dfs(grid, i, j - 1)
            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)

        for j in range(n):
            dfs(grid, 0, j)
            dfs(grid, m-1, j)

        for i in range(m):
            dfs(grid, i, 0)
            dfs(grid, i, n-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 1

        return res

# Method 2 - almost same
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return False

            grid[i][j] = 0
            dfs(i+1, j)
            dfs(i, j + 1)
            dfs(i-1, j)
            dfs(i, j - 1)

            return True

        for i in range(m):
            dfs(i,  0)
            dfs(i, n-1)

        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 1

        return res
