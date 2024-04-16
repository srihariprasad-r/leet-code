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
    
# Method 2 
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt =  0
        def bs(n):
            n.sort()
            l = -1
            r = len(n)-1

            while l < r:
                mid = l + (r-l+1)//2

                if n[mid] >= 0:
                    r = mid - 1
                else:
                    l = mid
            
            return l+1

        for i in range(len(grid)):
            cnt += bs(grid[i])

        return cnt