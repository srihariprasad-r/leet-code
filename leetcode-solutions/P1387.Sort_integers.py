class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power = [0] * (hi-lo+1)
        rge = [i for i in range(lo, hi+1)]

        def f(x, cnt):
            if x == 1: return cnt

            if x % 2 == 0: 
                return f(x// 2, cnt + 1)
            else:
                return f(3*x + 1, cnt +1)
        
        for i in range(len(rge)):
            power[i] = f(rge[i], 0)

        newlst = [x for _,x in sorted(zip(power, rge))]

        return newlst[k-1]