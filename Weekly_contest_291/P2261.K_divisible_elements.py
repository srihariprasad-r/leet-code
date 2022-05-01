class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        i = j = 0
        ans = set()
        
        for i in range(len(nums)):
            cnt = 0
            res = []
            for j in range(i, len(nums)):
                res.append(nums[j])
                if nums[j] % p == 0:
                    cnt  += 1
                    
                if cnt > k:
                    break
                
                # converted to tuple due to unhashable list
                ans.add(tuple(res))
        
        return len(ans)