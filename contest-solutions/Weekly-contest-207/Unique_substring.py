class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.ans = 0
        seen  = set()
        
        def recursion(idx):
            if idx == len(s):
                self.ans = max(self.ans, len(seen))
                return
            
            for i in range(idx,len(s)):
                if s[idx:i+1] not in seen:
                    seen.add(s[idx:i+1])
                    recursion(i+1)
                    seen.remove(s[idx:i+1])
                    
            return self.ans
        
        return recursion(0)