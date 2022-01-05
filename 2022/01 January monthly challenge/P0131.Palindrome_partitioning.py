class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        prt = []
        
        def ispalindrome(s, m, n):
            while m < n:
                if s[m] != s[n]:
                    return False
                m, n = m + 1, n-1
            return True
                
        def dfs(i):
            if i >= len(s):
                res.append(prt[:])
                return
            for j in range(i, len(s)):
                if ispalindrome(s, i, j):
                    prt.append(s[i:j+1])
                    dfs(j+1)
                    prt.pop()
        
        dfs(0)
        return res