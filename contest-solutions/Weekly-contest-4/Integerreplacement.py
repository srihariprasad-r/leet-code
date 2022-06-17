class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = {}
        def func(n, res):
            cnt = 0
            if n in res:
                return res[n]
            
            if n == 1:
                return 0
            elif n %2 == 0:
                cnt = func(n//2, res)+1
            else:
                cnt = min(func(n-1, res), func(n+1, res)) + 1
        
            if n not in res:
                res[n] = cnt
    
            return cnt
        return func(n, res)