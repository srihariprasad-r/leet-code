class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[0 for i in range(len(s))] for _ in range(len(s))]

        for g in range(len(s)):
            j = g
            for i in range(len(s)):
                if j >= i and j < len(s):
                    if g == 0:
                        dp[i][j] = 1                    
                    elif g == 1:
                        if s[i] == s[j]:
                            dp[i][j] = 1
                    else:
                        if s[i] == s[j] and dp[i+1][j-1] == 1:
                            dp[i][j] = 1
                    j += 1
        
        mp = collections.defaultdict(list)
        for g in range(len(s)):
            j = g
            for i in range(len(s)):
                if j >= i and j < len(s):
                    if g == 0:
                        mp[g].append(s[i])
                    else:
                        for k in range(i+1, j):
                            if dp[i][k]:
                                mp[g].append(s[i:k+1])
                            if dp[k+1][j]:
                                mp[g].append(s[k+1:j+1])
                j += 1

        res = []

        for r in mp.keys():
            res.append(mp[r])

        return res