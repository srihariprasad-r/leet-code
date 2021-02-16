class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        def dfs(i, n,res):
            if i > n:
                return
            else:
                res.append(i)
                for j in range(0, 10):
                    dfs(i*10+j,n,res)
                
        for i in range(1,10):
            dfs(i, n,res)
            
        return res