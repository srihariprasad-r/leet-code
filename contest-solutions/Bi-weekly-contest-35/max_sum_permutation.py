# TLE

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        events = [0] * len(nums)
        ans = 0

        for start, end in requests:
            for i in range(start, end+1):
                events[i] += 1

        events.sort(reverse=True)
        nums.sort(reverse=True)

        for i, x in enumerate(nums):
            ans += x * events[i]

        return ans % (10**9+7)
