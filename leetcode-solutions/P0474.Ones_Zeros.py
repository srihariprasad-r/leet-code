# wrong submission

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def dfs(idx, s, i, j, res):
            if idx >= len(s):
                return res, i, j
            
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
                ans, res_i, res_j = dfs(idx+1, s, i , j, res)
            
            return ans, res_i, res_j
        
        less = 0
        eql = 0
        more = 0
        
        for i in range(len(strs)):
            a, ans_i, ans_j = dfs(0, strs[i], 0, 0, 0)

            if a != float('inf'):
                if ans_i < m or ans_j < n:
                    less += 1
                elif ans_i == m or ans_j == n:
                    eql += 1
                else:
                    more += 1

        if less > eql: 
            return less
        else:
            return eql