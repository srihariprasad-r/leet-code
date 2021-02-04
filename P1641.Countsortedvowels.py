class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr= ['a', 'e', 'i', 'o', 'u']
        dp_arr = [[0 for i in range(len(arr))] for j in range(n+1)] 
        
        for i in range(n+1):
            for j in range(len(arr)):
                if i == 1:
                    dp_arr[i][j] = 1
                elif j == len(arr) - 1 and i != 0:
                    dp_arr[i][j] = 1

        for i in range(1, n+1):
            for j in range(len(arr)-2, -1, -1):
                dp_arr[i][j] = dp_arr[i-1][j] + dp_arr[i][j+1]
            
        return sum(dp_arr[n])