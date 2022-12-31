# wrong submission

class Solution:
    def minSwaps(self, s: str) -> int:
        s = [i for i in s]
        swp = 0
        i = 0
        j = len(s) - 1

        while i < j:
            if not(s[i] == '[' and s[i+1] == ']') or not(s[j-1] == '[' and s[j] == ']'):
                swp += 1
                s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return swp
