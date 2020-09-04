class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        sep = ""
        
        if n%1000 == n:
            return str(n)
        else:
            group = []
            str_n = str(n)
            while str_n:
                group.append(str_n[-3:])
                str_n = str_n[:-3]
            
            return str_n + '.'.join(reversed(group))                