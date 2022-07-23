class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dp(r1, c1, r2, c2):
            if (r1, c1, r2, c2) in memo:
                return memo[(r1, c1, r2, c2)]
            
            if r1 > n- 1 or c1 > n - 1 or r2 > n - 1 or c2 > n - 1 \
                or grid[r1][c1]  == -1 or grid[r2][c2] == -1:
                return -sys.maxsize
            
            if r1 == c1 == n- 1:
                return grid[r1][c1]
            
            cherry = 0
            
            if r1 == r2 and c1 == c2:
                cherry = grid[r1][c1]
            else:
                cherry = grid[r1][c1] + grid[r2][c2]
                
            new_cherry = - sys.maxsize
            
            directions = [(1, 0), (0, 1)]
            
            for d1 in directions:
                for d2 in directions:
                    nr1 = r1  + d1[0]
                    nc1 = c1 + d1[1]
                    nr2 = r2 + d2[0]
                    nc2 = c2 + d2[1]
                    
                    new_cherry = max(new_cherry, dp(nr1, nc1, nr2, nc2))
                    
            cherry = cherry + new_cherry
            memo[(r1, c1, r2, c2)] = cherry
            return cherry
        
        memo = {}
        n = len(grid)
        ans = dp(0, 0, 0, 0)
        
        return ans if ans > 0 else 0