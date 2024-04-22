class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def bs(x):
            cnt = 0
            for p in piles:
                q, r = p // x, p % x
                if r != 0:
                    cnt += 1
                cnt += q

            return cnt <= h

        l = 1
        r = max(piles)

        while l < r:
            mid = l + (r-l)//2

            if bs(mid):
                r = mid
            else:
                l = mid + 1

        return l