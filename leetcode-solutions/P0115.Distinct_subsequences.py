class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]

        for i in range(len(s)+1):
            dp[i][0] = 1

        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[len(s)][len(t)]

# TLE
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ans = 0
        def recurse(i, j):
            if j < 0: return 1
            if i < 0 : return 0

            a = 0
            if s[i] == t[j]:
                a += recurse(i-1, j-1) + recurse(i-1, j)
            else:
                a += recurse(i-1, j)

            return a

        return recurse(len(s)-1, len(t)-1)
