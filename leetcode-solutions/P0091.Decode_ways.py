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
    
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        dp = [0 for _ in range(len(s))]

        def recursion(idx):
            if idx == len(s): return 1

            one_digit = 0
            two_digit = 0

            if dp[idx] != 0: return dp[idx]

            if '1' <= s[idx] <= '9':
                one_digit += recursion(idx+1)

            if idx < len(s) - 1:
                if ((s[idx] == '1' and ('0' <= s[idx+1] <= '9')) or (s[idx] == '2' and ('0' <= s[idx+1] <= '6'))):
                    two_digit += recursion(idx+2)

            dp[idx] = one_digit + two_digit

            return one_digit + two_digit

        return recursion(0)            