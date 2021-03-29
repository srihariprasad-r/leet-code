class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = [0] * n
        xor = [0] * n
        for i in range(n):
            nums[i] = start + 2 * i

        xor[0] = nums[0]
        
        for j in range(1, len(nums)): 
            xored_value = xor[j-1] ^ nums[j]
            xor[j] = xored_value
        
        return xor[-1]