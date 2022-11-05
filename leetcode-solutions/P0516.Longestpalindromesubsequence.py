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

# Method 2

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def dfs(st, end, dp):
            if st > end:
                return 0
            
            # if st == end:
            #     return 1
            
            if dp[st][end] > 0: return dp[st][end]
            
            if s[st] == s[end]:
                dp[st][end] = 2 + dfs(st+1, end - 1, dp)
            else:
                dp[st][end] = max(dfs(st, end-1, dp), dfs(st+1, end, dp))
            
            return dp[st][end]
            
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(s)):
            for j in range(len(s)):
                if i == j:
                    dp[i][j] = 1
                    
        return dfs(0, len(s)-1, dp)