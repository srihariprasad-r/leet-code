class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def dfs(m):
            if m == 1:
                return 1

            res = 0 if m == n else m

            for i in range(1, m):
                s = dfs(i) * dfs(m-i)
                res = max(s, res)

            return res

        return dfs(n)
