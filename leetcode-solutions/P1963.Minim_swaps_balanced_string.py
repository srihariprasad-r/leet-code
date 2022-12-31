# wrong submission

class Solution:
    def minSwaps(self, s: str) -> int:
        swap = 0
        mx = 0
        for i in range(len(s)):
            if s[i] == '[':
                swap -= 1
            else:
                swap += 1
            mx = max(mx, swap)

        return (mx+1)//2 # every operation will remove a pair of balanced brackets
