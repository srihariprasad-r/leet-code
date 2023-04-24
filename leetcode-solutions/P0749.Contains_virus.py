# wrong submission

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        res = float('-inf')

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 0

            if grid[i][j] == 1: return 0

            grid[i][j] = 1

            return 1 + dfs(grid , i + 1, j) + dfs(grid, i, j + 1) \
                + dfs(grid, i, j - 1) + dfs(grid, i - 1, j)

        for i in range(len(isInfected)):
            for j in range(len(isInfected[0])):
                if isInfected[i][j] == 0:
                    res = max(res, dfs(isInfected, i, j))

        return res