# wrong submission

class Solution:
    def minSteps(self, n: int) -> int:
        def dfs(idx, n):
            if idx == n:
                return 1

            if idx > n:
                return 0

            take = 2 + dfs(idx+1, n)
            no_take = 1 + dfs(idx+1, n)

            return min(take, float('inf') if no_take == 0 else no_take)

        return dfs(0, n)
