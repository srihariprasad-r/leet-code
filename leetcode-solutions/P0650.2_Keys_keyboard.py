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

class Solution:
    def minSteps(self, n: int) -> int:
        def recursion(idx, c):
            if idx > n or c < 0: return 0
            
            take = float('inf')
            no_take = float('inf')

            if idx < c:
                take = 1 + recursion(idx+1, c//idx)
            if idx > c:
                no_take = 1 + recursion(idx+1, c)

            return min(take, no_take) 

        res = recursion(1, n)

        return 0 if res == float('inf') else res        