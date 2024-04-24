# wrong submission
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        ans = float('inf')

        def f(x):
            return sum(abs(a-x)*b for a, b in zip(nums, cost))

        l = 1
        r = 100000

        while l < r:
            mid = l + (r-l)//2
            if f(mid) < f(mid+1):
                ans = min(ans, f(mid))
                r = mid
            else:
                l = mid + 1

        return ans