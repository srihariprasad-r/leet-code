# wrong submission
class Solution:
    def minimizeStringValue(self, s: str) -> str:
        mp = collections.defaultdict(int)

        for c in s:
            if c =='?': continue
            mp[c] += 1
        
        s = list(s)

        for i in range(len(s)):
            if s[i] != '?': continue
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c not in mp:
                    mp[c] = 1
                    s[i] = c
                    break

        return ''.join(s)