class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_str = ""
        for c in s:
            if c.isalnum():     
                if ord(c) >= 65 and ord(c) <= 90:
                    c = chr(ord(c) +32)
                new_str += c

        p1 = 0
        p2 = len(new_str) - 1                
        while (p1 < p2):
            if new_str[p1] != new_str[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True        