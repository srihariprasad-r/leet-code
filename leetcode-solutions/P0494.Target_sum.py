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


# DP - memo

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def dfs(idx, s, dp):
            if idx >= n:
                if s == target:
                    return 1
                return 0

            key = (idx, s)
            if key in dp:
                return dp[key]

            take = dfs(idx+1, s + nums[idx], dp)
            no_take = dfs(idx+1, s - nums[idx], dp)

            dp[key] = take + no_take

            return dp[key]

        dp = {}

        return dfs(0, 0, dp)
