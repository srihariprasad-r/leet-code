class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) > len(s3): return False

        def recursion(i, j, k, st):
            if  k >= len(s3): 
                if st == s3: return True
                return False

            a = False
            b = False

            if i < len(s1):
                a = recursion(i+1, j, k+1, st + s1[i] if s1[i] == s3[k] else st)            
            if j < len(s2):
                 b = recursion(i, j+1, k+1, st + s2[j] if s2[j] == s3[k] else st)
            
            return False if not a and not b else True

        return recursion(0,0,0,'')          