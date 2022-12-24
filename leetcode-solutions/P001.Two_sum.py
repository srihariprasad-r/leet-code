class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.values = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):                
                if nums[i] ==  target - nums[j]:
                    return [i,j]

# Method 2

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if not(diff in mp):
                mp[nums[i]] = i
            else:
                ans= [mp[diff], i]

                return ans
            