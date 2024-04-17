# memory exceeded
class Solution:
    def arrangeCoins(self, n: int) -> int:
        arr = [i for i in range(n+1)]
        
        for idx in range(1, len(arr)):
            arr[idx] += arr[idx-1]

        def staircase(i):
            return arr[i]
        
        l = 1
        r = n

        while l < r:
            mid = l + (r-l+1)//2

            if staircase(mid) > n:
                r = mid - 1
            else:
                l = mid

        return l