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

# wrong submission
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = set()
        st = ''
        el = ''
        stck = []
        cnt = [0] * 26

        for i in s:
            cnt[ord(i) - ord('a')] += 1

        for c in s:
            while stck and ord(stck[-1]) >= ord(c) and cnt[ord(stck[-1]) - ord('a')] > 1:
                cnt[ord(stck[-1]) - ord('a')] -= 1
                stck.pop()
            stck.append(c)

        return ''.join(stck)