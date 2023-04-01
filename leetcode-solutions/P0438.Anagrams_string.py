class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(p)
        w = defaultdict(int)
        valid = 0

        res = []
        left = 0
        right = 0

        while right < len(s):
            c = s[right]
            if c in cnt:
                w[c] += 1
                if w[c] == cnt[c]:
                    valid += 1

            right += 1

            while right - left >= len(p):
                if valid == len(cnt):
                    res.append(left)
                d = s[left]
                left += 1
                if d in cnt:
                    if w[d] == cnt[d]:
                        valid -= 1
                    w[d] -= 1

        return res
