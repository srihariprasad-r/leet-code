class Solution:
    def minSteps(self, n: int) -> int:
        def dfs(s, c):
            if s == n: return 0
            if s > n: return float('inf')
            
            take = 2 + dfs(s+s, s)
            no_take = float('inf')
            if c:
                no_take = 1 + dfs(s+c, c)
            
            return min(take, no_take)
        
        return dfs(1, 0)
