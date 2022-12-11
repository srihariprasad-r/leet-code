# wrong submission

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        def dfs(idx, tgt, cnt=0):
            if idx == len(nums):
                return 0
            
            if nums[idx] == tgt:
                return 0
            
            take = float('-inf')
            no_take = float('-inf')
            
            take = 1 + dfs(idx+1, tgt * tgt, cnt + 1)
            no_take = dfs(idx+1, tgt, cnt)  
            
            return max(take, no_take)

        return dfs(0,nums[0]* nums[0], 0)


# Algorithms Casts

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        dp = collections.defaultdict(int)

        for num in range(len(nums)):
            dp[nums[num]] = dp[nums[num] * nums[num]] + 1

        return -1 if max(v for v in dp.values()) < 2 else max(v for v in dp.values())
