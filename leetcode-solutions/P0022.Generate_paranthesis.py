class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = []
        res = []
        def dfs(open, close):
            if open == close and close == n:
                res.append(''.join(copy.deepcopy(s)))
                return

            if open < n:
                s.append('(')
                dfs(open + 1, close)
                s.pop()
            
            if close < open:
                s.append(')')
                dfs(open, close + 1)
                s.pop()

            return res

        return dfs(0, 0)