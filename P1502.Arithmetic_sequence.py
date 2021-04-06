class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        progression = set() 
        for i in range(1, len(arr)):
            progression.add(abs(arr[i] - arr[i-1]))
        
        return True if len(progression) <= 1 else False