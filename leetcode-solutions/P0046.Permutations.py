class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for _ in range(len(nums)):
            el = nums.pop(0)
            sublists = self.permute(nums)

            for sublist in sublists:
                sublist.append(el)

            res.extend(sublists)
            nums.append(el)

        return res

# Method 2

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        arr = []
        n = len(nums)

        def dfs(idx):
            if idx == n:
                res.append(copy.deepcopy(nums))
                return
            
            for i in range(idx, n):
                nums[i], nums[idx] = nums[idx], nums[i]
                dfs(idx+1) 
                nums[i], nums[idx] = nums[idx], nums[i]
                
            return res