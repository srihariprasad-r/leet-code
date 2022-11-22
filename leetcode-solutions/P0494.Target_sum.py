# TLE

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def dfs(idx, s):
            if idx >= n:
                if s == target:
                    return 1
                return 0

            positive = dfs(idx+1, s + nums[idx])
            negative = dfs(idx+1, s - nums[idx])

            return positive + negative

        return dfs(0, 0)


# DP - memo fails

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def dfs(idx, s, dp):
            if s < 0 or s > target:
                return 0

            if idx >= n:
                if s == target:
                    dp[idx][s] = 1
                    return 1
                else:
                    return 0

            if dp[idx][s] != 0:
                return dp[idx][s]

            dp[idx][s] = dfs(idx+1, s + nums[idx], dp) + \
                dfs(idx+1, s - nums[idx], dp)

            return dp[idx][s]

        dp = [[0 for _ in range(target+1)] for _ in range(len(nums)+1)]

        return dfs(0, 0, dp)