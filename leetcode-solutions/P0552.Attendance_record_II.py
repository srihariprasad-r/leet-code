# TLE
class Solution:
    def checkRecord(self, n: int) -> int:
        def solve(n, absent, consecutivelate):
            if ((absent >= 2) or (consecutivelate >= 3)):return 0
            if n == 0: return 1            

            a = solve(n-1, absent + 1, 0)
            l = solve(n-1, absent, consecutivelate+1)
            p = solve(n-1, absent, 0)

            return a + l + p

        return solve(n, 0, 0)