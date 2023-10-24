class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
    
        return dp.get(n)
        
# Method 2

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = 0
        
        def recursion(n):
            if n < 0:
                return 0
            
            if n == 0:
                return 1
            
            ans = recursion(n-1) + recursion(n-2)
        
            return ans
        
        return recursion(n) 
        
# Method 3
class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(m, dp):
            if m < 0:
                return 0

            if m == 0:
                dp[m] = 1
                return dp[m]

            if dp[m] > 0:
                return dp[m]

            dp[m] += dfs(m-2, dp) + dfs(m-1, dp)

            return dp[m]

        dp = [0 for _ in range(n+1)]

        return dfs(n, dp)

# Method 4 
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)

        def recurse(n):
            if n < 0: return 0

            if n == 0:
                return 1

            if dp[n] > 0: return dp[n]

            dp[n] += recurse(n-1)
            dp[n] += recurse(n-2)

            return dp[n]

        return recurse(n-1) + recurse(n-2)