class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict

        cnt = Counter(t)
        w = defaultdict(int)
        valid = 0
        # need it to save left valid window pointer
        start = 0
        res = float('inf')

        left = 0
        right = 0

        while right < len(s):
            c = s[right]
            if c in cnt:
                w[c] += 1
                if w[c] == cnt[c]:
                    valid += 1

            right += 1

            while valid == len(cnt):
                if right - left < res:
                    start = left
                    res =  right - left
                d = s[left]
                left += 1
                if d in cnt:
                    if w[d] == cnt[d]: 
                        valid -= 1
                    w[d] -= 1

        return "" if res == float('inf') else s[start:start+res]