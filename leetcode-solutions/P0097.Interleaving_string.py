class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) > len(s3): return False
        
        def recursion(i, j, k, st):
            if  k >= len(s3): 
                if st == s3: return True
                return False

            if i >= len(s1) and j < len(s2): return False
            if i < len(s1) and j >= len(s2): return False

            take = False

            if s1[i] == s3[k]:
                return recursion(i+1, j, k+1, st + s1[i])
            else:
                return recursion(i, j+1, k+1, st + s2[j])

            return False

        return recursion(0,0,0,'')            