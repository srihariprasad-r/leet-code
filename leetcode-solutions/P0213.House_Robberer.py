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
            
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
      
        n = len(nums)            

        dp = [[-1 for _ in range(2)] for _ in range(len(nums))]

        def f(idx, s):  
            if s == 0 and idx == len(nums) - 1: return 0  

            if idx >= len(nums):
                return 0
            
            if dp[idx][s] != -1: return dp[idx][s]

            steal = 0
            no_steal = 0
            steal  = nums[idx] + f(idx+2, s)
            no_steal = f(idx+1, s)

            dp[idx][s]  = max(steal, no_steal)

            return dp[idx][s]

        mx1 = f(0, 0)
        mx2 = f(1, 1)

        return max(mx1, mx2)                                         