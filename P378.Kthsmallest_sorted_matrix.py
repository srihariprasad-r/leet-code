class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        newlist = [j for i in matrix for j in i]
        
        newlist.sort()
        return newlist[k-1]