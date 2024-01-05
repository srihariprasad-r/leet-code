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

# wrong submission
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def recurse(i, j):
            if i > 0 and j < 0: return False
            if i < 0 and j > 0:
                return all(True for a in s if a == '*')
            if i < 0 and j < 0: return True

            if s[i] == s[j] or s[j] == '?':
                return recurse(i-1, j-1)
            else:
                return recurse(i-1,j) or recurse(i, j-1)

        return recurse(len(s)-1, len(p)-1)