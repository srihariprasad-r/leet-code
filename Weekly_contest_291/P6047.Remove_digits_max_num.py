class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        def recursion(idx, n, max_el):
            if idx == len(n):
                return str(max_el)
            
            if int(n[idx]) == int(digit):
                max_el = max(max_el, int(n[0:idx] + n[idx+1:]))
            
            return recursion(idx+1, n, max_el)
            
        return recursion(0, number, 0)