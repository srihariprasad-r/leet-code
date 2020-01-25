class Solution(object):
    def isPalindrome(self,x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        a_pointer = 0
        b_pointer = len(x)-1
        while(a_pointer <= b_pointer):
            if x[a_pointer] != x[b_pointer]:
                return False
            a_pointer += 1
            b_pointer -= 1
        return True