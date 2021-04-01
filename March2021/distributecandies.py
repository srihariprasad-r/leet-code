class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        n = len(candyType)/2
        
        distinctcandies = set(candyType)
        
        if n < len(distinctcandies):
            return n
        else:
            return len(distinctcandies)