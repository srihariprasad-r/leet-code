class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sm = sum(stones)

        dp = [[float('inf') for _ in range(sm+1)] for _ in range(len(stones))]

        def recursion(idx, s):
            if idx >= len(stones): return abs(2*s-sm)

            if dp[idx][s] != float('inf'): return dp[idx][s]

            take = recursion(idx+1, s + stones[idx])
            no_take = recursion(idx+1, s)

            dp[idx][s] = min(take, no_take)

            return dp[idx][s]

        return recursion(0, 0)