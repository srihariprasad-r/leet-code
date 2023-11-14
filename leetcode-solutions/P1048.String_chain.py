class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        res = 0

        for word in words:
            dp[word] = 1

        words = sorted(words, key=lambda x:-len(x))

        for word in words:
            for w in range(len(word)):
                c = word[:w] + word[w+1:]
                if c in dp:
                    dp[c] = max(dp[c], dp[word] + 1)
                    
        return max(dp.values())