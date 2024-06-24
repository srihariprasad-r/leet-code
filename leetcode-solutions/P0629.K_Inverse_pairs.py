# wrong submission
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        res = 0

        dp = [[-1 for _ in range(k+1)] for _ in range(n+1)]

        for j in range(len(dp[0])):
            dp[0][j] = 0

        for i in range(len(dp)):
            dp[i][0] = 1

        def f(n, k):
            if n <= 0: return 0

            if k <= 0: 
                
                return 1

            if dp[n][k] != -1: return dp[n][k]

            result = 0
            for i in range(min(k, n-1)+1):
                result += f(n-1, k-i)

            dp[n][k] = result

            return dp[n][k]

        f(n, k)     
        return dp[n][k] 