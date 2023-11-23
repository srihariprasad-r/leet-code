class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def f(x):
            res = 0
            for q in quantities:
                qt = q // x
                r = q % x
                if r == 0: 
                    res += qt
                else: 
                    res += qt + 1
            return res <= n

        left = 1
        right = max(quantities)
        while left < right:
            mid = left + (right-left) //2
            if f(mid): 
                right = mid
            else: 
                left = mid + 1

        return left