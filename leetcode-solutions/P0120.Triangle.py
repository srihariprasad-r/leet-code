class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        def recursion(i, j, m, n, triangle, dp):
            if i == m - 1:
                return triangle[i][j]
            
            if dp[i][j] > float('-inf'): return dp[i][j]
            
            down = triangle[i][j] + recursion(i+1, j, m, n, triangle, dp)
            right = triangle[i][j] + recursion(i+1, j + 1, m, n, triangle, dp)
            
            dp[i][j] = min(down, right)
            
            return dp[i][j]
        
        m = len(triangle)
                     
        dp = [[float('-inf') for _ in range(m)] for _ in range(m)]
        
        return recursion(0, 0, m, m,  triangle, dp)


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i-1]
                                      [j-(j == i)], triangle[i-1][j-(j > 0)])

        return min(triangle[-1])


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1 for _ in range(len(triangle))] for _ in range(len(triangle))]
        def recurse(i, j):
            if i == n-1: return triangle[i][j]

            if i > n-1 or j > n-1: return float('inf')
            if dp[i][j] != -1: return dp[i][j]

            up = triangle[i][j] + recurse(i+1, j)
            left = triangle[i][j] + recurse(i+1, j+1)

            dp[i][j] = min(up, left)

            return dp[i][j]

        return recurse(0,0) 