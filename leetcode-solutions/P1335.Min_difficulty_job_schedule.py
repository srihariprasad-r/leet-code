class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d: return -1 

        def recursion(idx, s):            
            mx = float('-inf')
            finalRes = float('inf')

            if idx >= len(jobDifficulty) or s < 1: return 0

            if s == 1: 
                for i in range(idx, len(jobDifficulty)):
                    mx = max(mx, jobDifficulty[i])
                return mx

            for i in range(idx, len(jobDifficulty)-s+1):
                mx = max(mx, jobDifficulty[i])
                res = mx + recursion(i+1, s-1)
                finalRes = min(finalRes, res)

            return finalRes
        
        return recursion(0, d)