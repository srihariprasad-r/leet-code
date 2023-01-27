# TLE

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        while True:
            cnt = 1
            removed = False
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    cnt += 1
                else:
                    cnt = 1
                if cnt == k:
                    s = s[:i-k+1] + s[i+1:]
                    removed = True
                    cnt = 1
                    break
            if not removed:
                break
        return s

# Method 2 - wrong submission

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        mp = set()
        stck = []
        i = 0
        while i < len(s):
            if s[i] not in mp:
                mp.add(s[i])
                stck.append((s[i], 1))
            else:
                el , cnt = stck.pop()
                if el == s[i]:
                    if cnt + 1 == k:
                        while stck and stck[-1][0] == el:
                            stck.pop()
                        s = s[:i-k+1] + s[i+1:]
                        i = i - k
                    else:
                        stck.append((el, cnt + 1))
                else:
                    stck.append((el, cnt))
            i += 1

        return s
                
# Method - 3

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
