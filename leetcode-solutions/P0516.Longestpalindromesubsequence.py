class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
    
        for g in range(len(s)):
            j = g
            for i in range(len(s)):
                if g == 0:
                    dp[i][j] = 1
                elif g == 1:
                    if s[i] == s[j]:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = 2 + dp[i+1][j-1]
                    else:
                        dp[i][j] = max(dp[i][j-1],dp[i+1][j])
                    
                if j < len(s) - 1:
                    j += 1 
                else:
                    break
                    
        return dp[0][len(s)-1]