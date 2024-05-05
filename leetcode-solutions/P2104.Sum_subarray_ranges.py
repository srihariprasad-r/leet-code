class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        s = 0

        for i in range(len(nums)):
            mn_val = float('inf')
            mx_val = float('-inf')
            for j in range(i, len(nums)):
                mn_val = min(mn_val, nums[j])
                mx_val = max(mx_val, nums[j])
                diff = mx_val - mn_val
                s += diff

        return s