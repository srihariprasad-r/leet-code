class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    
        for i in range(len(dp)-1, -1, -1):
            for j in range(len(dp[0])-1, -1, -1):
                if i == len(dp) -1 and j == len(dp[0]) -1:
                    dp[i][j] = 0
                elif i == len(dp) -1:
                    dp[i][j] = ord(s2[j])+dp[i][j+1]
                elif j == len(dp[0]) -1:
                    dp[i][j] = ord(s1[i])+dp[i+1][j]
                else:
                    if s1[i] == s2[j]:
                        dp[i][j] = dp[i+1][j+1]
                    else:
                        dp[i][j] =  min(ord(s2[j])+dp[i][j+1], ord(s1[i])+dp[i+1][j])
        
        return dp[0][0]