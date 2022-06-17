class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        cnt = 0
        rows = [0] * m
        cols = [0] * n
        
        for x, y in indices:
            rows[x] += 1
            cols[y] += 1
        
        for i in range(m):
            for j in range(n):
                if (rows[i] + cols[j]) %2 != 0:
                    cnt += 1
                    
        return cnt