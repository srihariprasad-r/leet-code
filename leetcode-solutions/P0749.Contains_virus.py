# wrong submission

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        res = 0

        def contaminate(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return

            if grid[i][j] == 1: return

            grid[i][j] = 1 
            
            contaminate(grid , i + 1, j)
            contaminate(grid, i, j + 1)
            contaminate(grid, i, j - 1)
            contaminate(grid, i - 1, j)

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 0

            if grid[i][j] == 1: return 0

            grid[i][j] = 0

            return 1 + dfs(grid , i + 1, j) + dfs(grid, i, j + 1) \
                + dfs(grid, i, j - 1) + dfs(grid, i - 1, j)

        for i in range(len(isInfected)):
            contaminate(isInfected, i, 0)
            contaminate(isInfected, i, len(isInfected[0])-1)

        for j in range(len(isInfected[0])):
            contaminate(isInfected, 0, j)
            contaminate(isInfected, len(isInfected)-1, j)

        for i in range(len(isInfected)):
            for j in range(len(isInfected[0])):
                if isInfected[i][j] == 0:
                    res = max(res, dfs(isInfected, i, j))

        return res