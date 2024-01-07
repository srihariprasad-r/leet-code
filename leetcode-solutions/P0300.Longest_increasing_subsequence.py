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

# Method 2
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mx = float('-inf')
        if len(set(nums)) == 1: return 1
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for pre_idx in range(0, i):
                if nums[i] > nums[pre_idx]:
                    dp[i] = max(dp[i], dp[pre_idx]  + 1)
                    mx = max(mx, dp[i])

        return 1 if mx == float('-inf') else mx