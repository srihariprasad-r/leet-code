class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        ans = 0
        c = [0] * 61
        for x in time:
            m = x % 60
            ans += c[60 - m]
            c[m if m else 60] += 1
        return ans
