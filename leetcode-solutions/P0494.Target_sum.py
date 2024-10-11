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


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def recursion(idx, s):
            if idx < 0 and s == 0: return 1                
            if (idx < 0): return 0

            pos = recursion(idx-1, s + nums[idx])
            neg = recursion(idx-1, s - nums[idx])

            return pos + neg

        return recursion(len(nums)-1, target)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def recurse(idx, s):
            if idx >= len(nums): 
                if s == target: return 1
                return 0

            return recurse(idx+1, s + nums[idx]) + recurse(idx+1, s - nums[idx])

        return recurse(0, 0)        