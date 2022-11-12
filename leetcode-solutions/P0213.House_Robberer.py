# wrong submission

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(idx, s, a, dp):
            if idx >= n:
                return s
            
            if dp[idx] > 0: return dp[idx]
            
            take = float('-inf')
            no_take = float('-inf')
            
            if not a or (a and (not((idx+1)%n in a))):
                take = dfs(idx + 2, s + nums[idx], a + [idx], dp)
            no_take = dfs(idx + 1, s, a, dp)
            
            dp[idx] = max(take, no_take)
            
            return dp[idx]
        
        dp = [0] * (n+1)
        
        return dfs(0,0, [], dp)
            
            