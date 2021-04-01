class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_tmp = list(filter(lambda x: x %2 == 0, A))
        odd_tmp = list(filter(lambda x: x %2 != 0, A))
        
        return even_tmp + odd_tmp