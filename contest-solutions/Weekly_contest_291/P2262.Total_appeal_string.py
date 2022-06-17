class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0] * (n+1) 
        last_idx = [-1] * 26
        ans = 0
        
        for i in range(len(s)):
            c = ord(s[i]) - ord('a')
            dp[i+1] = dp[i] +i - last_idx[c]
            ans += dp[i+1]
            last_idx[c] = i
            
        return ans