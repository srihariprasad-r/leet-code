class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def dfs(idx, s, i, j, res):
            if idx >= len(s):
                return res
            
            ans = 0   
                
            if idx < len(s):
                if s[idx] == '0' and i < m: 
                    i += 1
                    res += 1
                elif s[idx] == '1' and j < n: 
                    j += 1
                    res += 1
                else:
                    res = float('inf')
                ans += dfs(idx+1, s, i , j, res)
            
            return ans
        
        o = []
        
        for i in range(len(strs)):
            a = dfs(0, strs[i], 0, 0, 0)
            if a != float('inf'): o.append(a)
            
        return len(o)