class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 1;
        for i in range(0, len(nums)-1):
            if (nums[i] != nums[i+1]):
                nums[index] = nums[i+1]
                index += 1
        
        return index

# Method 2

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                tmp = nums[left + 1]
                nums[left + 1] = nums[right]
                nums[right] = nums[left + 1]
                left = left + 1
                right += 1
        
        return left + 1
        