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

# Method 2
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recursion(l, r, arr):
            if l < 0 or r < 0 or l > r:
                return

            if l == 0 and r == 0:
                res.append(copy.deepcopy(''.join(arr)))
                return

            arr.append('(')
            recursion(l - 1, r, arr)
            arr.pop()

            arr.append(')')
            recursion(l, r - 1, arr)
            arr.pop()

            return res

        return recursion(n, n, [])
