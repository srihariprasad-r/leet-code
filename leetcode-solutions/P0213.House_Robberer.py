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
            
# wrong submission
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        n = len(nums)
        # if n % 2 == 0:
        #     nums = nums + [nums[0]]

        def f(idx):            
            if idx >= len(nums):
                return 0
            
            steal = 0
            no_steal = 0
            steal  = nums[idx] + f(idx+2)
            no_steal = f(idx+1)

            return max(steal, no_steal)

        mx1= float('-inf')
        mx2 = float('-inf')
        if n % 2 == 0:
            mx1 = f(0)
        else:
            mx2 = f(1)

        return max(mx1, mx2)                            