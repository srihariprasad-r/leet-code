class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)

        dp = [[0] * (n+1) for _ in range(m+1)]

        # word2 is null, delete every char from word1
        # delete char from word1 at i will be i-1 and j will remain
        # so dp[i-1][0]
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + 1

        # word1 is null, insert every char from word2
        # insert char from word2, if after insert char at i == j; use i-1/j-1
        # this is because there is no operation can be done
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] + 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                # i -1 since i represents length and not index
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + 1,  # delete from word1
                                   dp[i][j-1] + 1,  # insert in word1, so same char does not contribute
                                   dp[i-1][j-1] + 1  # replace word in word1, same char does not contribute
                                )

        return dp[-1][-1]