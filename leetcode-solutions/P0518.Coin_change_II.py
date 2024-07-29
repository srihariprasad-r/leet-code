class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if len(coins) == 0 or amount <= 0:
            return 1

        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]

        for i in range(len(coins)):
            dp[i][0] = 1

        for i in range(len(coins)):
            include = 0
            exclude = 0
            for j in range(1, amount+1):
                if j >= coins[i]:
                    include = dp[i][j-coins[i]]
                if i > 0:
                    exclude = dp[i-1][j]
                dp[i][j] = include + exclude

        return dp[-1][-1] if dp[-1][-1] > -1 else 0


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def recursion(idx, tot):
            if tot < 0 or idx < 0: return 0
            if tot == 0: return 1

            pick = 0
            if coins[idx] <= tot:
                pick = recursion(idx,tot-coins[idx])
            no_pick = recursion(idx-1, tot)

            return pick + no_pick

        return recursion(len(coins)-1, amount)            