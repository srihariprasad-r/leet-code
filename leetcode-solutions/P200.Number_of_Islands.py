class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if grid is None or len(grid) == 0:
            return 0
        
        numOfIslands = 0
        
        def gridSelection(grid, i, j):
            if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0'):
                return 0
            
            grid[i][j] = '0'
            
            gridSelection(grid, i + 1, j)
            gridSelection(grid, i-1, j)
            gridSelection(grid, i, j + 1)
            gridSelection(grid, i, j-1)
            
            return 1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == '1'):
                    numOfIslands += gridSelection(grid, i, j)
        
        return numOfIslands                    