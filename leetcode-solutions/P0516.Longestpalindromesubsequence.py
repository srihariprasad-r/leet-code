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

# generate all subsets
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        ans = []

        def palindrome(st):
            i = 0
            j = len(st) - 1

            while i < j:
                if not st[i] == st[j]:
                    return False
                
                i += 1
                j -= 1
            
            return True

        def recurse(idx, arr):
            ans.append(''.join(arr))

            for i in range(idx, len(s)):
                arr.append(s[i])
                recurse(i+1, arr)
                arr.pop()

            return ans

        o = recurse(0, [])
        # print(o)
        mx = float('-inf')
        
        for i in range(len(o)):
            if palindrome(o[i]):
                mx = max(mx, len(o[i]))

        return mx

# Memonization
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
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
        
        return lcs(len(s1)-1 , len(s1)-1)