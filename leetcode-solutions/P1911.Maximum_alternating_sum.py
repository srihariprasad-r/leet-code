class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        msum = float('-inf')
        def recurse(idx, flag):
            if idx >= len(nums):
                return 0

            c = nums[idx]
            if flag : c *= -1

            take = recurse(idx+1, not flag) + c

            no_take = recurse(idx+1, flag)

            return max(take, no_take)

        return recurse(0, False)            