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
        