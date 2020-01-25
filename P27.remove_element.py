class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cnt = nums.count(val)
        
        if cnt == 1:
            nums.remove(val)
            return len(nums)
        elif cnt > 1:
            while(cnt > 0):
                nums.remove(val)
                cnt -= 1
        else:
            return len(nums)
    
        return len(nums)