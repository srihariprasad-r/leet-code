class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def f(n):
            cnt = 0
            for c in candies:
                cnt += c // n
                if cnt >= k:
                    return True
            
            return False

        if sum(candies) < k: return 0

        l = 1
        r = max(candies)

        while l < r:
            mid = r - (r-l) // 2

            if f(mid):
                l = mid
            else:
                r = mid - 1

        return l