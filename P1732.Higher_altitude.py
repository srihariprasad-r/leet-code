class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        after_gain = [0]

        for i in range(len(gain)):
            after_gain.insert(i+1, after_gain[i] + gain[i])
        
        return max(after_gain)