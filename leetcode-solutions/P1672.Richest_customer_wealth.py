class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxsum = 0
        for i in range(len(accounts)):
            maxsum = max(maxsum, sum(accounts[i]))
        
        return maxsum