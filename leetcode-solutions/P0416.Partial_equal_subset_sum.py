class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        if sum(nums) % 2:
            return False
        # py3
        @cache
        def dfs(idx, s):
            if idx == n:
                return s == 0

            if s < 0:
                return False

            return dfs(idx + 1, s - nums[idx]) or dfs(idx + 1, s)

        partial_sum = sum(nums)/2

        return dfs(0, partial_sum)

# Method 2

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        if sum(nums) % 2 :
            return False
        
        def recursion(idx, target, dp):
            if idx == 0:
                if target == 0:
                    return True
                else:
                    return False
                
            if target == 0:
                return True
            
            if nums[idx] == target:
                return True
            
            if dp[idx][target] != -1 : return dp[idx][target]
            
            not_take = recursion(idx-1, target, dp)
            take = recursion(idx-1, target - nums[idx], dp)
            
            dp[idx][target] = take or not_take
            
            return dp[idx][target]
        
        target = sum(nums)//2
        dp = [[-1 for _ in range(target+1)] for _ in range(n+1) ]
        
        return recursion(n-1,target, dp)

# Method 3
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)

        if sm%2: return False

        sm = sm // 2
        dp = [[False] * (sm + 1) for _ in range(len(nums)+1)]

        for i in range(len(nums)+1):
            dp[i][0] = True

        for i in range(1,len(nums)+1):
            for j in range(1, sm + 1):
                if j - nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

        return dp[-1][-1]