class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x: x[1])

        dp = [1] * len(pairs)

        for i in range(len(pairs)-1, 0, -1):
            for j in range(i-1, -1, -1):
                if pairs[i][0] > pairs[j][1]:
                    dp[j] = dp[i] + 1

        return dp[0]        