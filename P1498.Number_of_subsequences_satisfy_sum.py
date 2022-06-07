class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        mod = 10**9+7
        n = len(nums)
        l = ans = 0
        r = n - 1

        while l <= r:
            if nums[l] + nums[r] <= target:
                ans += pow(2, r - l, mod)
                l += 1
            else:
                r -= 1

        return ans % mod
