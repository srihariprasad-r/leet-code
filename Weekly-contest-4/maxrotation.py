class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sumtotal = sum(A)
        f0_sum, maxsum = 0, 0
    
        for idx, el in enumerate(A):
            f0_sum += idx * el
        
        maxsum = f0_sum
        
        for i in range(1,len(A)):
            f0_sum = f0_sum + sumtotal - len(A)*A[len(A)-i]
            if maxsum < f0_sum:
                maxsum = f0_sum
    
        return maxsum