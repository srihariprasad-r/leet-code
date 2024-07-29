class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1 for i in range(amount+1)]

        dp[0] = 0

        for i in range(1, len(dp)):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]] + 1)

        if amount < dp[-1]:
            return -1
        else:
            return dp[amount]

# Method 2 - wrong submission


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 0 or amount <= 0:
            return 0

        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]

        for i in range(len(coins)):
            dp[i][0] = 0

        for i in range(len(coins)):
            include = float('inf')
            exclude = float('inf')
            for j in range(1, amount+1):
                if j >= coins[i]:
                    include = 1 + dp[i][j-coins[i]]
                if i > 0:
                    exclude = dp[i-1][j]
                dp[i][j] = min(include, exclude)

        return dp[-1][-1]

# Method 3 - wrong submission

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        
        def dfs(idx, amt, dp):
            if idx == len(coins): 
                if amt < 0 or amt > 0 : return float('inf')
                return 0
    
            if dp[amt] > -1: return dp[amt] 

            if amt == 0: return 0
            if amt < 0: return float('inf')

            take = float('inf')
            no_take = float('inf')

            if coins[idx] <= amt:
                take = 1 + dfs(idx, amt - coins[idx], dp)
            no_take = dfs(idx+1, amt, dp)

            dp[amt]  = min(take, no_take)
            return dp[amt] 

        dp = [-1 for _ in range(amount+1)]
        dfs(0, amount, dp)
        return -1 if dp[-1] == float('inf') else dp[-1]
    

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf')] * (amount+1) for _ in range(len(coins)+1)]

        for i in range(len(coins)+1):
            dp[i][0] = 0

        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if j - coins[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i][j-coins[i-1]] + 1, dp[i-1][j])

        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins, key=lambda x:x)
        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
        def recursion(idx, tot, ct):
            if tot < 0 or idx < 0: return float('inf')
            if tot == 0: return ct
            if idx == 0:
                return ct + (tot//coins[idx]) if tot%coins[idx] == 0 else float('inf')

            if dp[idx][tot] != -1:
                return dp[idx][tot]

            pick = float('inf')
            if coins[idx] <= tot: 
                pick = recursion(idx, tot-coins[idx], ct + 1)
            no_pick = recursion(idx-1, tot, ct)                

            dp[idx][tot] = min(pick, no_pick)
            return min(pick, no_pick)

        res = recursion(len(coins)-1, amount, 0)
        return res if res != float('inf') else -1        