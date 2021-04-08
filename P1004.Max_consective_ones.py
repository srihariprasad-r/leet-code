class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        cnt = 0
        j = 0
        res = 0
        for i in range(len(A)):
            if A[i] == 0:
                cnt += 1
            while cnt > K:
                if A[j] == 0: cnt -= 1
                j += 1
            res = max(res, i - j + 1)
        
        return res