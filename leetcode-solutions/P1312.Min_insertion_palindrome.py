class Solution:
    def minInsertions(self, s: str) -> int:
        s1 = s
        s2 = s[::-1]

        dp = [[-1 for _ in range(len(s1))] for _ in range(len(s1))]

        def lcs(i, j):
            if i < 0 or j < 0: return 0

            if dp[i][j] > -1: return dp[i][j]
            
            c = 0
            if s1[i] == s2[j]:
                c = 1 + lcs(i-1, j-1)
            else:
                c += max(lcs(i, j-1), lcs(i-1,j))

            dp[i][j] = c
            return c
        
        return len(s) - lcs(len(s1)-1 , len(s1)-1)