class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """    
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        cnt = 0
    
        for g in range(len(s)):
            j = g
            for i in range(len(s)):
                if g == 0:
                    dp[i][j] = True
                    cnt += 1
                elif g == 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        cnt += 1
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True      
                        cnt += 1
                                
                        
                if j < len(s) - 1:
                    j += 1
                else:
                    break

        return cnt

# Method 2

class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0

        for i in range(len(s)):
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1

            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1

        return cnt
