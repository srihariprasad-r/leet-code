# TLE

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """        
        def isPalindrome(i, j, s):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
                
            return True
        
        def f(idx, dp):
            if idx == len(s):
                return 0
            
            if dp[idx] != -1: return dp[idx]
            
            ans = float('inf')
            
            for j in range(idx, len(s)):
                if isPalindrome(idx, j, s):
                    cost = 1 + f(j+1, dp)
                    ans = min(cost, ans)
                    dp[idx] = ans
                    
            return dp[idx]

        dp = [-1] * len(s)
        return f(0, dp) - 1

class Solution:
    def minCut(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        f_arr = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for g in range(len(s)):
            j = g
            for i in range(len(s)):
                if j >= i and j < len(s):
                    if g == 0: dp[i][j] = 1
                    elif g == 1:
                        if s[i] == s[j]:
                            dp[i][j] = 1
                    else:
                        if s[i] == s[j] and dp[i+1][j-1]:
                            dp[i][j] = 1
                j += 1                        

        for g in range(len(s)):
            j = g
            for i in range(len(s)):
                if j >= i and j < len(s):
                    if g == 0: f_arr[i][j] = 0
                    elif g == 1:
                        if s[i] == s[j]:
                            f_arr[i][j] = 0
                    else:  
                        if dp[i][j]: f_arr[i][j] = 0
                        else:
                            mn = float('inf')
                            for k in range(i, j):                      
                                left = f_arr[i][k]
                                right = f_arr[k+1][j]
                                mn = min(mn, left+right+1)

                            f_arr[i][j] = mn
                j += 1    
        
        return f_arr[0][len(s)-1]               

class Solution:
    def minCut(self, s: str) -> int:
        res = float('inf')

        def palindrome(st):
            i = 0 
            j = len(st) - 1

            while i <= j:
                if st[i] != st[j]: 
                    return False

                i += 1
                j -= 1
            
            return True

        def recurse(i, j, res):
            if ((i > j) or (j >= len(s))) : return 0

            if palindrome(s[i:j+1]): return 0

            pc1 = float('inf')
            pc2 = float('inf')

            for k in range(i, j):
                pc1 = recurse(i, k, res)                
                pc2 = recurse(k+1, j, res)
                res = min(res, 1+pc1+ pc2)

            return res
        
        return recurse(0, len(s)-1, res)        