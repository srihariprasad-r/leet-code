class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        dp = [[[0] * 2 for _ in range(len(s)+1) ] for _ in range(len(t)+1)]

        st = 0

        for i in range(1,len(t)+1):
            for j in range(1,len(s)+1):
                if t[i-1] == s[j-1]:
                    dp[i][j][0] = dp[i-1][j-1][0] + 1
                    dp[i][j][1] = dp[i-1][j-1][1]
                else:
                    dp[i][j][0] = 0
                    dp[i][j][1] = dp[i-1][j-1][0] + 1
        
                st += dp[i][j][1]
        
        return st