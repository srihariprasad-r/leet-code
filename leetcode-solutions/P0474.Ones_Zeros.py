# TLE

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def dfs(idx, i, j):
            if idx == len(strs):
                return 0

            take = float('-inf')
            no_take = float('-inf')

            cnt_i = strs[idx].count('0')
            cnt_j = strs[idx].count('1')
            if i - cnt_i >= 0 and j - cnt_j >= 0:
                take = 1 + dfs(idx+1, i - cnt_i, j - cnt_j)
            no_take = dfs(idx+1, i, j)

            return max(take, no_take)

        return dfs(0, m, n)

# DP - wrong submission


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def dfs(idx, i, j, dp):
            if idx == len(strs):
                return 0

            y = (idx, i, j)
            if y in dp:
                return dp[y]

            cnt_i = strs[idx].count('0')
            cnt_j = strs[idx].count('1')

            dp[y] = dfs(idx+1, i, j, dp)

            if i - cnt_i >= 0 and j - cnt_j >= 0:
                dp[y] = max(dp[y], 1 + dfs(idx+1, i - cnt_i, j - cnt_j, dp))

            return dp[y]

        dp = {}

        return dfs(0, m, n, dp)