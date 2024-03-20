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

# Method 2 - move outwards

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        ln = 0

        for i in range(len(s)):
            # odd length - "bab"
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > ln:
                    ln = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1

            # even length: "cbbd"
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > ln:
                    ln = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1

        return res

# Method 3:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        ans = 0
        mx = ''
        for i in range(len(s)):
            dp[i][i] = 1
            if ans < 1:
                ans = 1
                mx = s[i]

        l = 1
        i = 0
        while i < len(s) - 1:
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                if ans < 2 :
                    ans = 2
                    mx = s[i:i+ans]
            i += 1

        l = 3
        while l <= len(s):
            i = 0
            while i < len(s) - l + 1:
                j = i + l - 1
                if s[i] == s[j] and dp[i+1][j-1] == 1:
                    dp[i][j] = 1
                    mx = s[i:i+l]
                i += 1
            l += 1

        return mx



























