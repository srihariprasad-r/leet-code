class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def subfunc(s, l, r):
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            
            return ( r - l + 1 , l, r)
        
        longest = 0
        left = 0
        right = -1
            
        for i in range(len(s)):
            #odd check
            length , l , r = subfunc(s, i, i)
            if length > longest:
                longest = length
                left = l
                right = r
            
            #even check
            length , l , r = subfunc(s, i, i + 1)
            if length > longest:
                longest = length
                left = l
                right = r
        
        return s[left: right +1]                        