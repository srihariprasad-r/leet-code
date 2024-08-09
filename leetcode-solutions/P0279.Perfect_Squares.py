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


# Method 2

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(1,int((n)**0.5)+1)]

        q = []
        visited = set()
        q.append((n, 0, 0))
        visited.add(0)


        while q:
            el, s, d = q.pop(0)
            if s == el: return d
            for i in range(len(squares)):
                if s + squares[i] <= el:
                    if s + squares[i] not in visited:
                        q.append((el, s + squares[i], d + 1))
                        visited.add(s+squares[i])

        return d 


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)

        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            for j in range(1, int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i-j*j]+1)
        

        return dp[-1]