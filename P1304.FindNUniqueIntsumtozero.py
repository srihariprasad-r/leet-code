class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = []

        m = 0 
        
        for i in range(n//2, m, -1):
            arr.insert(i, i)
            arr.insert(i,-i)        
        
        if n%2 != 0:
            arr.insert(-1,0)
            
        return arr