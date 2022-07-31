class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if len(nums) == 1:
            return 1
        
#         if len(nums) == 2:
#             return 2
        
        max_idx = nums.index(max(nums)) 
        min_idx = nums.index(min(nums))
        
        tmp_max_idx = max_idx
        tmp_min_idx = min_idx
        
        # swap if i > j 
        if min_idx > max_idx:
            max_idx = tmp_min_idx
            min_idx = tmp_max_idx

        # three states:
        #1. x x i j x x x x <- i & j occurs at the front(delete all element upto index j = max_idx + 1 - 0 based adding 1)
        #2. x x x x x x i j  <- i & j at the back(delete from idx = i = n - min_idx)
        #3. x i x x x x j x <- both front and back(min_idx + 1 for idx i +  n - max_idx for j)
        return min(max_idx + 1 , n - min_idx , min_idx + 1 + n - max_idx)