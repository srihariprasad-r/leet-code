class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        st = 1
        jumps = 1
        balance = n
        left = True
        
        while balance > 1:
            if (left or balance % 2 == 1):
                st += jumps
            balance = balance/2
            jumps *= 2
            left = not(left)
            
        return st