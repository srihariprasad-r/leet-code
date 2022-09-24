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
