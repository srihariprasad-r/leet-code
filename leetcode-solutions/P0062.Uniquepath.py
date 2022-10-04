class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[-1 for i in range(n)] for j in range(m)]
    
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1] +  dp[i-1][j]
                
        return dp[-1][-1]


# Method 2 - TLE

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def dfs(i, j, cnt):
            if i == m -1  and j == n - 1:
                return 1
            
            if i > m -1 or j > n - 1:
                return 0
            
            return dfs(i, j+1, cnt + 1) + dfs(i+1, j, cnt + 1)
        
        return dfs(0,0,0)