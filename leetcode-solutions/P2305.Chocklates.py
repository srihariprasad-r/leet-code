class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        v = [0] * k
        global ans
        ans = float('inf')

        def backtrack(idx, v, s):
            if idx >= len(cookies):
                mn = float('-inf')
                mx = max(v)
                mnval = min(v)
                global ans
                mn = min(mn, mx - mnval)
                ans = min(ans, mx)
                return

            for i in range(k):
                v[i] += cookies[idx]
                backtrack(idx+1, v, s)
                v[i] -= cookies[idx]
                if v[i] == 0:
                    break

            return

        backtrack(0, v, 0)

        return ans