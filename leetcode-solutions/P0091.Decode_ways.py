class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0

        def dfs(idx, dp):
            if idx == len(s):
                return 1

            if idx > len(s) or s[idx] == '0':
                return 0

            if dp[idx] != -1:
                return dp[idx]

            res = dfs(idx+1, dp)

            if (idx < len(s) - 1 and ((s[idx] == '1' and s[idx+1] <= '9') or (s[idx+1] < '7' and s[idx] == '2'))):
                res += dfs(idx+2, dp)

            dp[idx] = res

            return res

        dp = [-1] * len(s)
        return dfs(0, dp)