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
                    