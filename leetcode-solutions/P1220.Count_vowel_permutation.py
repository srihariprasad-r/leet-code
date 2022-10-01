# TLE submission

class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = []
        fnl = []
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        mp = {
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a']
        }
        
        def dfs(idx, n, mp, v, cur):
            if idx < 0 or len(cur) > n:
                return
            
            if len(cur) == n:
                if cur not in res:
                    res.append(cur)
                    return
            
            for c in mp[v]:
                # mp[v].remove(c)
                dfs(idx-1, n, mp, c, cur + c)
                # mp[v].append(c)
                    
            return res
        
        for v in vowels:
            dfs(n, n, mp, v, v)

        return len(res)