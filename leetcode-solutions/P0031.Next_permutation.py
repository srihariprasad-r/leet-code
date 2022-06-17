class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        alreadySorted = False
        left = 0
        right = 1
        
        while right < len(nums):
            if nums[left] < nums[right]:
                left += 1
                right += 1
            else:
                break

        prevLeft = left -1
        prevRight = left
        
        newleft = left + 1 if right != len(nums) - 1 else len(nums) - 2
        newright = right + 1 if right != len(nums) - 1 else len(nums) - 1

        while newright < len(nums):
            if nums[newleft] < nums[newright]:
                alreadySorted = True
                nums[newleft], nums[newright] = nums[newright], nums[newleft]
                newleft += 1
                newright += 1
            else:
                newright += 1
        
        if not alreadySorted:
            nums[prevLeft], nums[prevRight] = nums[prevRight], nums[prevLeft]
        
            left = prevRight
            right = len(nums) - 1
        
            while left != right:
                if nums[left] > nums[right]:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1