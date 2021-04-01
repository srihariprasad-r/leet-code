class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        less_than_zero = 0
        for i in range(len(grid)):
            less_than_zero += len(list(filter(lambda x: x < 0, grid[i])))
        
        return less_than_zero