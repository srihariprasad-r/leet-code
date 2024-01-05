# Wrong submmission

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]

        dp[0][0] = True
        
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = True

        for i in range(1, m+1):
            for j in range(1, n+1):
                if (p[j-1] == '?' or (s[i-1] == p[j-1])):
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

        return dp[-1][-1]

# TLE
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[-1 for _ in range(len(p))] for _ in range(len(s))]
        def recurse(i, j):
            if i < 0 and j < 0: 
                return True
            if i >= 0 and j < 0: 
                return False
            if i < 0 and j >= 0:
                for a in range(j+1): 
                    if p[a] != '*':
                        return False
                return True
                # return all(True for a in s if a == '*')

            if dp[i][j] != -1: return dp[i][j]

            if (s[i] == p[j]) or (p[j] == '?'):
                dp[i][j] =  recurse(i-1, j-1)
            elif p[j] == '*':
                dp[i][j] =  recurse(i,j-1) or recurse(i-1, j)
            else:
                dp[i][j] = False

            return dp[i][j]
                    
            # return False

        return recurse(len(s)-1, len(p)-1)