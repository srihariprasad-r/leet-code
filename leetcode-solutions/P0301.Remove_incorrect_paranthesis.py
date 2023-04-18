# TLE

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        mx = float('-inf')
        ans = set()

        def valid(p):
            cnt = 0

            if p.count('(') != p.count(')'): return False

            for i in range(len(p)):
                if p[i].isalpha(): continue
                
                if p[i] == '(': 
                    cnt += 1
                else: 
                    cnt -= 1
                    if cnt < 0: return False

            return True

        def dfs(idx, arr):
            if idx == len(s):
                res.append(copy.deepcopy(''.join(arr)))
                return

            arr.append(s[idx])
            dfs(idx+1, arr)
            arr.pop()
            if s[idx] != '(' or s[idx] != ')': dfs(idx+1, arr)

            return res

        result = dfs(0, [])
        for r in result:
            if valid(r):
                ans.add(r)
                mx = max(mx, len(r))

        return filter(lambda x: len(x) == mx, list(ans))