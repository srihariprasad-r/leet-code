class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t_p = 0
        s_p = 0 
        if len(s) == 0:
            return True
        while(t_p < len(t)):
            if (t[t_p] == s[s_p]):
                s_p += 1
                if (s_p == len(s)):
                    return True
            t_p += 1
        return False

# Method 2
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [False] * len(s)
        
        def recurse(i, j):
            if i < 0 or j < 0: return False

            if s[i] == t[j]:
                dp[i] = True
                recurse(i-1, j-1)
            else:
                recurse(i, j - 1)

            return True

        recurse(len(s)-1, len(t)-1)
        
        return False if dp.count(True) != len(dp) else True