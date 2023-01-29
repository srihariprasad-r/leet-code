class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import sys
        s3 = -sys.maxsize
        stck = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < s3:
                return True
            while len(stck) > 0 and stck[-1] < nums[i]:
                val = stck.pop()
                s3 = max(s3, val)
        
            stck.append(nums[i])      
        return False

# Method 2 - slightly different to above

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stck = []
        v = float('-inf')
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < v: 
                return True

            while stck and stck[-1] < nums[i]:
                v = stck[-1]
                stck.pop()

            stck.append(nums[i])

        return False