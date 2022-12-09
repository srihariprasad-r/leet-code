class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ans.append(bin(i)[2:].count('1'))

        return ans

# Method 2 - DP

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [-1] * (n+1)
        dp[0] = 0
        r = 1
        for i in range(1, n+1):
            if r * 2 == i:
                r *= 2
            dp[i] = dp[i-r] + 1

        return dp