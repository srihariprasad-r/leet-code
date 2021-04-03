class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        def ispalindrome(s):
            i = 0
            j = len(s) -1
            while i <j :
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        if len(s) == 0:
            return 0
        else:
            if ispalindrome(s):
                return 1
            else:
                return 2