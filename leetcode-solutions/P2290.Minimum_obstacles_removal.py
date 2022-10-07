# Run time error

class Solution(object):
    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def recursion(i, j, m, n, grid, dp):
            if (i < 0 or i > m - 1 or j < 0 or j > n - 1):
                return 0

            if grid[i][j]:
                return 1

            if i == 0 and j == 0:
                return grid[i][j]

            if dp[i][j] > -1:
                return dp[i][j]

            # up, left, right, down = 0, 0, 0, 0

            up = recursion(i-1, j, m, n, grid, dp)
            left = recursion(i, j-1, m, n, grid, dp)
            right = recursion(i, j + 1, m, n, grid, dp)
            down = recursion(i+1, j, m, n, grid, dp)

            dp[i][j] = up + left + right + down + 0 if not grid[i][j] else 1

            return dp[i][j]

        m = len(grid)
        n = len(grid[0])

        dp = [[-1 for _ in range(n)] for _ in range(m)]

        return recursion(m-1, n-1, m, n, grid, dp)
