# wrong submission

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        sqnums = [i * i for i in range(1, n+1) if i * i <= n]

        def dfs(idx, cnt, n, res, dp):
            if idx == len(sqnums):
                return 0

            if n < 0:
                return 0

            if n == 0:
                return cnt

            if dp[idx] != -1:
                return dp[idx]

            take = dfs(idx, cnt+1, n - sqnums[idx], res, dp)
            not_take = dfs(idx+1, cnt, n, res, dp)

            if take == 0:
                take = float('inf')
            if not_take == 0:
                not_take = float('inf')

            res = min(take, not_take)

            dp[idx] = res

            return dp[idx]

        dp = [-1 for _ in range(n)]

        return dfs(0, 0, n, float('inf'), dp)
