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

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def recurse(i, j, c):
            if i + j >= len(s3):
                if c == s3: return True
                return False

            take = False
            no_take = False
  
            if i < len(s1) and s1[i] == s3[i+j]:
                take = recurse(i+1, j, c + s1[i])            
            if j < len(s2) and s2[j] == s3[i+j]:
                no_take = recurse(i, j+1, c + s2[j])  

            return take or no_take
        
        return recurse(0,0,'')                    