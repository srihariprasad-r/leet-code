# wrong submission
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        ms = 0
        ans = [] 

        pleft = [0] * len(nums)
        pright = [len(nums)-k] * len(nums)

        p = [0] * len(nums)
        p[0] = nums[0]

        for i in range(1, len(nums)):
            p[i] = p[i-1] + nums[i]

        total = nums[k] - nums[0]
        for i in range(k, len(nums)):
            s = nums[i-k] - nums[i]
            if s > total:
                total = s
                pleft[i] = i - k
            else:
                pleft[i] = pleft[i-1]

        total = nums[len(nums)-1] - nums[len(nums)-1-k]
        for i in range(len(nums)-k-1, -1, -1):
            s = nums[i+k] - nums[i]
            if s >= total:
                total = s
                pright[i] = i + k
            else:
                pright[i] = pright[i+1]

        for i in range(k, len(nums)-(2*k)):
            l = pleft[i-1]
            r = pright[i+k]
            total = nums[i+k] - nums[i] + nums[l+k] - nums[l] + nums[r+k] - nums[r]
            if total >= ms:
                ans = [l, i, r]
                ms = total

        return ans