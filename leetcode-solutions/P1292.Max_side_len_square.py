class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])
        
        def f(idx):
            for i in range(m-idx+1):
                for j in range(n-idx+1):
                    if (presum[i][j] - presum[i+idx][j] - \
                    presum[i][j+idx] + presum[i+idx][j+idx]) <= threshold:
                        return True
                    
            return False
        
        presum = [[0]* (n+1) for _ in range(m+1)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                presum[i][j] = mat[i][j] + presum[i+1][j] + presum[i][j+1] - presum[i+1][j+1]
                
        l = 0
        r = min(m, n)
        
        while l < r:
            mid = l + (r-l+1)//2
            if f(mid):
                l = mid
            else:
                r = mid - 1
                
        return l