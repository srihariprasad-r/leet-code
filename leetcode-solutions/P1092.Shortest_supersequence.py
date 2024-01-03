# wrong submission

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [[0 for _ in range(len(str2))] for _ in range(len(str1))]

        # for i in range(len(str2)+1):
        #     dp[0][i] = 0

        # for i in range(len(str1)+1):
        #     dp[i][0] = 0

        def recursion(i, j):
            if i < 0 or j < 0 : return 0

            if dp[i][j] > 0: return dp[i][j]
            if str1[i] == str2[j]:
                dp[i][j] =  1 + recursion(i-1, j-1)
            else:
                dp[i][j] = max(recursion(i-1, j), recursion(i, j-1))
            
            return dp[i][j]

        recursion(len(str1)-1, len(str2)-1)
        
        m = len(str1)-1
        n = len(str2)-1
        c = ''

        while m >= 0 and n >= 0:
            if str1[m] == str2[n]:
                c += str1[m]
                m -= 1
                n -= 1
            elif dp[m-1][n] > dp[m][n-1]:
                c += str1[m] 
                m -= 1
            else:
                c += str2[n]
                n -= 1

        while m >= 0:
            c += str1[m]
            m -= 1

        while n >= 0:
            c += str2[n]
            n -= 1

        return c