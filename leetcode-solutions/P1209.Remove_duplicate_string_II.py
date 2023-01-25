class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stck = [[' ', 0]]

        for c in s:
            if stck[-1][0] == c:
                stck[-1][1] += 1
                if stck[-1][1] == k:
                    stck.pop()
            else:
                stck.append([c, 1])

        return ''.join([a*b for a, b in stck])
