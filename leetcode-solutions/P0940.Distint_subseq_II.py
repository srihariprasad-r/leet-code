# TLE

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        ans = []
        def subseq(idx, st):
            if st not in ans and len(st) > 0: ans.append(st)

            for i in range(idx, len(s)):
                st += s[i]
                subseq(i+1, st)
                st = st[0:-1]

            return ans

        return len(subseq(0,'')) % (100_000_000 + 7)