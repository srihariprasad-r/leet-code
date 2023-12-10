class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque

        q = deque()
        
        dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    
        dp[-1][-1] = 1
    
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                if i == len(grid)-1 : 
                    if j < len(grid[0])-1:
                        dp[i][j] = dp[i][j+1] + grid[i][j]
                elif j == len(grid[0])-1:
                    if i < len(grid)-1:
                        dp[i][j] = dp[i+1][j] + grid[i][j]
                else:
                    if dp[i+1][j] < dp[i][j+1]:
                        dp[i][j] = grid[i][j] + dp[i+1][j]
                    else:
                        dp[i][j] = grid[i][j] + dp[i][j+1]
                    
        q.append((0, 0, str(grid[0][0])))
        result = []
    
        while len(q) > 0:
            el = q.popleft()
            i_index, j_index, strn = el[0], el[1], el[2]
            if i_index == len(dp) - 1 and j_index == len(dp[0]) -1:
                return sum(int(i) for i in strn.split('->'))
            elif i_index == len(dp) - 1:
                q.append((i_index, j_index+1, str(grid[i_index][j_index+1])+'->'+strn))
            elif j_index == len(dp[0]) - 1:
                q.append((i_index+1, j_index, str(grid[i_index+1][j_index])+'->'+strn))
            else:
                if (dp[i_index][j_index] + dp[i_index+1][j_index] < 
                    dp[i_index][j_index] + dp[i_index][j_index+1]):
                    q.append((i_index+1, j_index, str(grid[i_index+1][j_index])+'->'+strn))
                elif (dp[i_index][j_index] + dp[i_index+1][j_index] > 
                      dp[i_index][j_index] + dp[i_index][j_index+1]):
                    q.append((i_index, j_index+1, str(grid[i_index][j_index+1])+'->'+strn))
                else:
                    q.append((i_index+1, j_index, str(grid[i_index+1][j_index])+'->'+strn))
                    q.append((i_index, j_index+1, str(grid[i_index][j_index+1])+'->'+strn))


# Method 2
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def recursion(i, j, m, n, grid, dp):
            if i == 0 and j == 0:
                return grid[i][j]
            
            if i < 0 or i > m - 1 or j < 0 or j > n - 1:
                return float('inf')
            
            if dp[i][j] > 0 : return dp[i][j]
            
            up = grid[i][j] + recursion(i-1, j, m, n, grid, dp)
            left = grid[i][j] + recursion(i, j - 1, m, n, grid, dp)
            
            dp[i][j] = min(up, left)
            
            return dp[i][j]
        
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        return recursion(m-1, n-1, m, n, grid, dp)


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]

        def recurse(i, j, sm):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return float('inf')

            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                dp[i][j] = sm + grid[i][j]
                return dp[i][j]

            if dp[i][j] != 0:
                return dp[i][j]

            dp[i][j] = grid[i][j] + \
                min(recurse(i+1, j, sm), recurse(i, j+1, sm))

            return dp[i][j]

        return recurse(0, 0, 0)

# Method 2
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[0]) for _ in range(len(grid))] 

        def recurse(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return float('inf')
            
            if i == 0 and j == 0: return grid[i][j]

            if dp[i][j] > 0: return dp[i][j]

            up = grid[i][j] + recurse(i-1, j)
            left = grid[i][j] + recurse(i, j-1)

            dp[i][j] = min(up, left)

            return dp[i][j]

        return recurse(len(grid)-1, len(grid[0])-1)

