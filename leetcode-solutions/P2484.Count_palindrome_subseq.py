# wrong submission

class Solution:
    def countPalindromes(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for g in range(len(s)):
            j = g
            for i in range(len(s)):
                if g == 0:
                    dp[i][j] = 1
                elif g == 1:
                    if s[i] == s[j]: 
                        dp[i][j] = 3
                    else:
                        dp[i][j] = 2
                else:
                    if g == 4:
                        if s[i] == s[j]:
                            dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1
                        else:
                            dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
                    
                if j < len(s)-1: 
                    j += 1
                else:
                    break

        return dp[0][4]