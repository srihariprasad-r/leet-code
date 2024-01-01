# TLE

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # s = ''.join(set(list(c for c in s)))
        used = [0] * len(s)
        ans = []
        def subseq(idx, st):
            if st not in ans and len(st) > 0: ans.append(st)

            for i in range(idx, len(s)):
                if used[i]: continue
                if i > idx and s[i] == s[i-1] and not used[i-1]: continue
                st += s[i]
                used[i] = 1
                subseq(i+1, st)
                st = st[0:-1]
                used[i] = 0

            return ans

        return len(subseq(0,'')) % (100_000_000 + 7)