class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        odds = []
        for i in range(len(arr)+1):
            cnt = 0 
            while i % 2 != 0 and cnt <= len(arr) - 1:
                if i == 1:
                    odds.append(arr[cnt])
                else:
                    if cnt + i <= len(arr) :
                        odds.append(sum(arr[cnt:i+cnt]))

                cnt += 1
        
        return sum(odds)