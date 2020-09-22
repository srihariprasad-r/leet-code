class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        dp = [0] * (N + 1)
        
        for i in range(2, N+1):
            for j in range(1, i):
                if i%j == 0 and dp[i-j] == 0:                    
                    dp[i] = 1

        return dp[N]
                