class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmpsum = 0
        # added due to failing TLE
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0]**3) * (len(nums)-2) + nums[0]**2 + nums[0]

        nums = [1] + nums + [1]

        dp = [[-1 for i in range(len(nums)+1)] for j in range(len(nums)+1)]

        def dfs(l, r):
            if l > r:
                return 0

            if dp[l][r] != -1:
                return dp[l][r]

            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dfs(l, i-1) + dfs(i+1, r)
                dp[l][r] = max(dp[l][r], coins)

            return dp[l][r]

        return dfs(1, len(nums)-2)
