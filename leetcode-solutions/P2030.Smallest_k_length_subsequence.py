class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        cnt = s.count(letter)
        stck = []

        for idx, c in enumerate(s):
            while stck and ((stck[-1] > c and len(stck) + len(s) - idx > k \
                and (stck[-1] != letter or \
                cnt > repetition)) or k - len(stck) < repetition):
                el = stck.pop()
                if el == letter:
                    repetition += 1

            if len(stck) < k:
                stck.append(c)
                if c == letter:
                    repetition -= 1

            if c == letter:
                cnt -= 1

        return ''.join(stck)
