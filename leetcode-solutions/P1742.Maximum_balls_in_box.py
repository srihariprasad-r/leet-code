class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        n = highLimit - lowLimit + 1
        box = [0] * 46
        mx = 0
        for i in range(lowLimit, highLimit + 1):
            m = 0
            while i > 0:
                m += i % 10
                i = i//10
            box[m] += 1
            mx = max(box[m], mx)
        
        return mx