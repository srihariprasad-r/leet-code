# wrong submission
class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        powersOf5 = [format(5**i,'b')  for i in range(15)]
        dp = [0] * len(s)

        dp[0] = 1 if s[0] == '1' else 0

        for i in range(1,len(s)):
            j = i
            t = s[j]
            if s[i] == '0': continue
            v = float('inf')
            while j > -1:
                if str(t) in powersOf5:  
                    v = min(v, 1 + dp[j-1])
                j -= 1
                t += s[j]
            dp[i] =  v
        
        return dp[len(s)-1] if dp[len(s)-1] != 0 else -1