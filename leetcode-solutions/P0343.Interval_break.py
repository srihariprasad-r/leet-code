#  wrong submission (DP memonization - fails)

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs(idx, n, s, mx, ar):
            if s == n:
                mx = reduce(lambda x, y: x * y, ar)
                return mx

            if s > n:
                return 1

            take = 1
            no_take = 1

            for i in range(idx, n):
                take = dfs(i, n, s + idx, mx, ar + [idx])
                no_take = dfs(i+1, n, s, mx, ar)

                mx = max(mx, max(take, no_take))

            return mx

        return dfs(1, n, 0, 1, [])
