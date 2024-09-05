class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        def recursion(idx, prev):
            if idx >= len(s): return 0

            flip = float('inf')
            no_flip = float('inf')

            if s[idx] == '0':
                if prev == '0':                                    
                    flip = 1 + recursion(idx+1, '1')
                    no_flip = recursion(idx+1, '0')
                elif prev == '1':
                    flip = 1 + recursion(idx+1, '1')   
            else:
                if prev == '0':                
                    flip = 1 + recursion(idx+1, '0')
                    no_flip = recursion(idx+1, '1')
                elif prev == '1':
                    no_flip = recursion(idx+1, '1')                  

            return min(flip, no_flip)

        return recursion(0, s[0])                     