class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        @lru_cache(None)
        def dp(r, c):
            if r == row-1 and c == col-1:
                return [grid[r][c], grid[r][c]]

            v1 , v2 = float('inf'), float('-inf')
        
            if r + 1 < row:
                a, b = dp(r+1, c)
                v1 = min(v1, a * grid[r][c], b * grid[r][c])
                v2 = max(v2, a * grid[r][c], b * grid[r][c])
            if c + 1 < col:
                a, b = dp(r, c+1)
                v1 = min(v1, a * grid[r][c], b * grid[r][c])
                v2 = max(v2, a * grid[r][c], b * grid[r][c])
                
            return [v1, v2]
        
        ans = max(dp(0, 0))
        
        if ans < 0: return -1 
        else: return ans % (10 ** 9 + 7)