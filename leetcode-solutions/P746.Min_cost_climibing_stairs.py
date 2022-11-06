class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * len(cost)
        
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
                
        return min(dp[-2], dp[-1])
        
# Method 2

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        def dfs(idx, c, dp):
            if idx >= n:
                return c

            if dp[idx] > 0:
                return dp[idx]

            dp[idx] = cost[idx] + min(dfs(idx+1, c, dp), dfs(idx+2, c, dp))

            return dp[idx]

        dp = [0 for _ in range(n)]

        return min(dfs(0, 0, dp), dfs(1, 0, dp))
