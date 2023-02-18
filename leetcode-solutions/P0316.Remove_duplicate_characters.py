class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stck = []
        lst_idx = Counter()

        for i in range(len(s)):
            lst_idx[s[i]] = i

        for i in range(len(s)):
            if s[i] not in stck:
                while stck and s[i] < stck[-1] and i < lst_idx[stck[-1]]:
                    stck.pop()
                stck.append(s[i])

        return ''.join(stck)
