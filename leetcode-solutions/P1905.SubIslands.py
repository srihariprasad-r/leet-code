class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        res = 0

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0

            if grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)

        # exclude islands in grid2 which are sea in grid1
        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    dfs(grid2, i, j)

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    dfs(grid2, i, j)
                    res += 1

        return res
    
# Method 2 - almost same
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        res = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] == 0:
                return

            grid2[i][j] = 0
            dfs(i+1, j)
            dfs(i, j + 1)
            dfs(i-1, j)
            dfs(i, j-1)

            return

        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    res += 1
                    dfs(i, j)

        return res