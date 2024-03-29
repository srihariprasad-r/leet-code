class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n  = 0
    
        left = [0, 0]
        right = [sum(nums[0::2]), sum(nums[1::2])]
    
        for i in range(len(nums)):
            right[i%2] -= nums[i]
            if left[0] + right[1] == right[0] + left[1] :
                n += 1
            left[i%2] += nums[i]
        
        return n

# Method 2:


class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0

        oddPreSum = [0] * (n+1)
        evenPreSum = [0] * (n+1)

        for i in range(len(nums)):
            if i % 2:
                oddPreSum[i+1] = oddPreSum[i] + nums[i]
                evenPreSum[i+1] = evenPreSum[i]
            else:
                oddPreSum[i+1] = oddPreSum[i]
                evenPreSum[i+1] = evenPreSum[i] + nums[i]

        for i in range(1, n+1):
            oddSum1 = oddPreSum[i-1]
            oddSum2 = evenPreSum[-1] - evenPreSum[i]

            evenSum1 = evenPreSum[i-1]
            evenSum2 = oddPreSum[-1] - oddPreSum[i]

            if oddSum1 + oddSum2 == evenSum1 + evenSum2:
                ans += 1

        return ans
