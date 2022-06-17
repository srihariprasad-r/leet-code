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