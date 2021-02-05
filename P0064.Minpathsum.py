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