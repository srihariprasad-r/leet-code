class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for x in A:
            if A.count(x) > 1:
                return x