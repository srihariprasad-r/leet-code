class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return
        
        n = len(nums)
        ptr1 = float('inf')
        
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                ptr1 = i - 1
                break
                
        if ptr1 != float('inf'):
            ptr2 = float('inf')
            
            for j in range(n-1, ptr1, -1):
                if nums[j] > nums[ptr1]:
                    ptr2 = j
                    break
                    
            nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
            reverse(ptr1+1,n-1)
            
        else:
            reverse(0, n-1)