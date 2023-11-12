class Solution:
    def largestVariance(self, s: str) -> int:
        res = 0

        def f(c1, c2):
            c_a = 0
            c_b = 0
            extend = False
            ans = 0
            for c in s:
                if c != c1 and c !=c2:
                    continue

                if c == c1:
                    c_a += 1
                else:
                    c_b += 1

                if c_b > c_a:
                    c_a = 0
                    c_b = 0
                    extend = True
                
                if c_b > 0:
                    ans = max(ans, c_a-c_b)
                elif c_b == 0 and extend is True:
                    ans = max(ans, c_a - 1)
                
            return ans

        for c1 in 'abcdefghijklmnopqrstuvwxyz':
            for c2 in 'abcdefghijklmnopqrstuvwxyz':
                res = max(res, f(c1, c2))

        return res