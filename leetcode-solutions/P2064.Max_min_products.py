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
    
# almost same
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def stores(x):
            cnt = 0
            for q in quantities:
                a, r = q//x, q%x
                if r != 0:
                    cnt += 1
            
                cnt += a
            
            return cnt <= n

        l = 1
        r = max(quantities)

        while l < r:
            mid = l + (r-l)//2
            if stores(mid):
                r = mid
            else:
                l = mid + 1
            
        return l