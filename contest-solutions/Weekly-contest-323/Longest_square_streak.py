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