class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        msum = float('-inf')
        def recurse(idx, arr, flag, o_sum, e_sum, msum):    
            if idx >= len(arr):
                return msum

            take = 0
            no_take = 0
            if not flag:
                if idx % 2: o_sum += nums[idx]
                else: e_sum += nums[idx]
                msum = max(msum, abs(o_sum - e_sum))
                take = recurse(idx+1, arr, flag, o_sum, e_sum, msum)
            else:
                arr = arr[idx:]
                msum = max(msum, abs(o_sum - e_sum))                
                no_take = recurse(idx,arr, not flag, o_sum, e_sum, msum)

            return max(take, no_take)

        return recurse(0, nums, 0, 0, 0, msum)            