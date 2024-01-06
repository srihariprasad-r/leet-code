class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    
        for i in range(len(nums)):
            res = max(res, dp[i])
            
        return res

# TLE
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mx = float('-inf')
        dp = [[0] * len(nums)]*len(nums)

        def recurse(idx, pre_idx):
            if idx >= len(nums):
                return 0

            if dp[idx][pre_idx+1] > 0: return dp[idx][pre_idx+1]

            no_take =  recurse(idx+1, pre_idx)
            take = float('-inf')
            if pre_idx == -1 or nums[idx] > nums[pre_idx]:
                take = 1 + recurse(idx+1, idx)

            mx = max(take, no_take)

            dp[idx][pre_idx+1] = mx

            return mx

        return recurse(0, -1) 