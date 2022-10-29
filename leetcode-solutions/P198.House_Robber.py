class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        if nums is None:
            return 0
        elif len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) > 2:
            dp.insert(0,nums[0])
            dp.insert(1,max(nums[0], nums[1]))
            for i in range(2,len(nums)):
                dp.insert(i,max(nums[i] + dp[i-2], dp[i-1]))
                
        #print(dp)        
        return dp[-1]

# Method 2
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def dfs(idx, dp):
            if idx == len(nums):
                return 0

            if idx > len(nums):
                return 0

            if dp[idx] != -1:
                return dp[idx]

            take = nums[idx] + dfs(idx+2, dp)
            not_take = dfs(idx+1, dp)

            dp[idx] = max(take, not_take)

            return dp[idx]

        dp = [-1] * len(nums)
        return dfs(0, dp)
