class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        s = [0] * len(piles)
        t = [0] * len(piles)
        dp = [[x for x in zip(s, t)] for _ in range(len(piles))]

        for i in range(len(piles)):
            dp[i][i] = (piles[i], 0)

        for i in range(len(piles)-2, -1, -1):
            for j in range(i+1, len(piles)):
                left = piles[i] + dp[i+1][j][1]
                right = piles[j] + dp[i][j-1][1]
                if left > right:
                    dp[i][j] = (left, dp[i+1][j][0])
                else:
                    dp[i][j] = (right, dp[i][j-1][0])

        return dp[0][-1][0] - dp[0][-1][1]