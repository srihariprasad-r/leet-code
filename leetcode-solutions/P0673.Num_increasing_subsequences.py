class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        dp = [[1]*2  for _ in range(len(nums))]        

        mx_len = 0 
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i][0] < dp[j][0] + 1:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                    elif dp[i][0] == dp[j][0] + 1:
                        dp[i][1] += dp[j][1]
                mx_len = max(mx_len, dp[i][0])
        
        s = 0
        for k in dp:
            if k[0] == mx_len: s += k[1]      

        return s