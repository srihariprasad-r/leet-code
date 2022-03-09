class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        if nums[left] < nums[right]: return nums[left]
        
        def minfind(start, end):
            while start < len(nums) and start < end:
                if nums[start] < nums[end]:
                    break
                else:
                    start += 1
                    # end -= 1
            return start
        
        while left +1 < right:
            mid = left + (right-left)//2
            if nums[mid] == nums[right]:
                if mid - 1 >= 0 and nums[mid-1] < nums[mid]:
                     left = mid - 1
                elif mid + 1 < len(nums) and nums[mid+1] < nums[mid]:
                     right = mid + 1
                else:
                    high = minfind(mid, right)
                    low = minfind(left, mid)
                    return min(nums[high], nums[low])

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return min(nums[left], nums[right])