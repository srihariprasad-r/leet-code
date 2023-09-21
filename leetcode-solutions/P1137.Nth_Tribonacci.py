class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        
        if n == 0: return 0
        if n <= 2 : return 1

        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        def t(idx):
            if idx > n: return float('inf')

            if dp[idx] != float('inf'): return dp[idx]

            dp[idx] = t(idx-3) + t(idx-2) + t(idx-1)

            return dp[idx]

        return t(n)