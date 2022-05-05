class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = sorted(set(nums))
        ans = float('inf')

        for i, st in enumerate(nums):
            end = st + n - 1
            idx = bisect_right(nums, end)
            ans = min(ans, n - (idx-i))

        return ans
