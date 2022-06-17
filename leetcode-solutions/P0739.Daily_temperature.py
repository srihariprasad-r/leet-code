class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        res = [0] * len(T)
        stck = []
        for i, val in enumerate(T):
            while len(stck) > 0 and T[i] > T[stck[-1]]:
                idx = stck.pop()
                res[idx] = i - idx
            stck.append(i)
        
    
        return res