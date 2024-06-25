# TLE
class Solution:
    def checkRecord(self, n: int) -> int:
        def solve(n, absent, consecutivelate):
            if ((absent >= 2) or (consecutivelate >= 3)):return 0
            if n == 0: return 1            

            a = solve(n-1, absent + 1, 0)
            l = solve(n-1, absent, consecutivelate+1)
            p = solve(n-1, absent, 0)

            return a + l + p

        return solve(n, 0, 0)

# wrong submission
class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]

        def solve(n, absent, consecutivelate):
            if ((absent >= 2) or (consecutivelate >= 3)): return 0
            if n == 0: return 1            
            
            if dp[n][absent][consecutivelate] != -1: return dp[n][absent][consecutivelate]

            a = solve(n-1, absent + 1, 0)  % 100_000_007   
            l = solve(n-1, absent, consecutivelate + 1)  % 100_000_007   
            p = solve(n-1, absent, 0)  % 100_000_007                

            dp[n][absent][consecutivelate] = (a + l + p) % 100_000_007            
            
            return dp[n][absent][consecutivelate]

        return solve(n, 0, 0)
