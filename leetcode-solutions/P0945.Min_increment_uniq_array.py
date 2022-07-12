class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums.sort()
        prev = nums[0]
        ans = 0

        for i in range(1, len(nums)):
            cur = nums[i]

            if cur <= prev:
                ans += prev - cur + 1
                cur = prev + 1

            prev = cur

        return ans
