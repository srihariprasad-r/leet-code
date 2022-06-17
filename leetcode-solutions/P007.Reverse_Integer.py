class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x <0 else 1
        x = abs(x)        
        output = pop = 0
        while(x != 0):
            pop = x %10            
            output = (output *10) + pop
            x = int(x /10)            
        
        if output > 2147483647:
            return 0
        else:
            return output * sign