class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = [[0] * 3 for _ in range(n+1)]

        def recurse(n, k):
            if k == 1: return n
            if n == 0: return 0

            if dp[n][k] != 0: return dp[n][k]

            res = float('inf')

            for i in range(1, n+1):
                res = min(res, max(recurse(n-i, k), recurse(i-1, k-1)) + 1)

            dp[n][k] = res

            return res

        return recurse(n, 2)