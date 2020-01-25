class Solution(object):
    def validPalindrome(self,s):
        """
        :type s: str
        :rtype: bool
        """
        a_pointer = 0
        b_pointer = len(s) -1      
        while(a_pointer <= b_pointer):
            if s[a_pointer] != s[b_pointer]:
                return self.substring_palindrome(s,a_pointer+1, b_pointer) or self.substring_palindrome(s,a_pointer, b_pointer-1)
            a_pointer += 1
            b_pointer -= 1
        
        return True
 
    def substring_palindrome(self,s,i,j):
        a_pointer = i
        b_pointer = j      
        while(a_pointer <= b_pointer):
            if s[a_pointer] != s[b_pointer]:
                return False
            a_pointer += 1
            b_pointer -= 1
        
        return True