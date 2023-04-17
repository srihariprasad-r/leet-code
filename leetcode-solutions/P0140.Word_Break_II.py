class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []

        def dfs(s, arr):
            if not s:
                res.append(arr.strip())
                return

            for w in wordDict:
                if s.startswith(w):
                    dfs(s[len(w):], arr + ' ' + w)

            return res

        return dfs(s, '')
