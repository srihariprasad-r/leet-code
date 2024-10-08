"""
Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table_list = []
        table_list.append(nums[0])
        max_value = nums[0]
        for i in range(1,len(nums)):
            max_value = max(nums[i]+max_value, nums[i])
            table_list.append(max_value)

        return max(table_list)
        
# Method 2

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = float('-inf')
        sum = 0
        
        for i in range(len(nums)):
            sum += nums[i]
            sum = max(sum, nums[i])
            mx = max(mx, sum)
            
        return mx

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[-1]

        csum = 0
        osum = float('-inf')

        for i in range(len(nums)):            
            csum = max(nums[i], csum + nums[i])
            osum = max(osum, csum)

        return osum        