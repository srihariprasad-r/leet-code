class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[len(text1)][len(text2)]

# Method 2
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]

        for i in range(len(text2)-1, -1, -1):
            for j in range(len(text1)-1, -1, -1):
                if text2[i] == text1[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])


        return dp[0][0] 

# TLE
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mx = float('-inf')
        def recurse(i, j):
            if i < 0 or j < 0:
                return 0

            if text1[i] == text2[j]:
                return 1 + recurse(i-1, j-1)
            else:
                return max(recurse(i, j-1),recurse(i-1, j))

        return recurse(len(text1)-1, len(text2)-1)

# Memonization
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        def recurse(i, j, dp):
            if i < 0 or j < 0:
                return 0

            if dp[i][j] > -1: return dp[i][j]

            a = float('-inf')
            if text1[i] == text2[j]:
                a =  1 + max(a, recurse(i-1, j-1, dp))
            else:
                l = recurse(i, j-1, dp)
                r = recurse(i-1, j, dp)
                a = max(a, max(l,r))

            dp[i][j] = a

            return dp[i][j]

        return recurse(len(text1)-1, len(text2)-1, dp)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text1)+1)] for _ in range(len(text2)+1)]
        mx = float('-inf')

        for i in range(len(dp)-2,-1, -1):
            for j in range(len(dp[0])-2,-1, -1):                
                if text2[i] == text1[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

                mx = max(mx, dp[i][j])

        return mx        