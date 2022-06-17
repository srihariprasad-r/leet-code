class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(row, col1, col2):
            if (row, col1, col2) in memo:
                return memo[(row, col1, col2)]
        
            if row == m:
                return 0

            cherries_at_level = grid[row][col1] + (0 if col1 == col2 else grid[row][col2])
            maxres = 0
            
            for i in range(-1,2):
                for j in range(-1,2):
                    new_col1 = col1 + i
                    new_col2 = col2 + j
                    
                    if 0 <= new_col1 < n and 0 <= new_col2 < n:
                        maxres = max(maxres, dfs(row+1, new_col1, new_col2))
            
            res = maxres + cherries_at_level
            memo[(row, col1, col2)] = res
            
            return res
            
        memo = {}
        m = len(grid)
        n = len(grid[0])
        
        return dfs(0, 0, n-1)