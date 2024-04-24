class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        ans = float('inf')

        def f(x):
            return sum(abs(a-x)*b for a, b in zip(nums, cost))

        l = min(nums)
        r = max(nums)

        while l < r:
            mid = l + (r-l)//2
            y1 = f(mid)
            y2 = f(mid+1)
            ans = min(ans, min(y1, y2))
            if y1 < y2:
                r = mid
            else:
                l = mid + 1

        return ans if ans != float('inf') else 0