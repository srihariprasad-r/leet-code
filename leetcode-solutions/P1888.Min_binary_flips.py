# wrong submission

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        s1, s2 = '', ''
        d1, d2 = 0, 0
        ans = float('inf')

        for i in range(len(s)):
            s1 += '0' if i % 2 else '1'
            s2 += '1' if i % 2 else '0'

        l = 0
        for r in range(len(s)):
            if s[r] != s1[r]:
                d1 += 1
            if s[r] != s2[r]:
                d2 += 1  

            if r - l + 1 > n:
                if s[l] != s1[l]:
                    d1 -= 1         
                if s[l] != s2[l]:
                    d2 -= 1
                l += 1

            if (r - l + 1) == n:
                ans = min(ans, min(d1, d2))

        return ans
