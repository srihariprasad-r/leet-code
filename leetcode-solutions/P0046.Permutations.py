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

# Method 3

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(fq, arr, res):
            if len(arr) == len(nums):
                if arr not in res:
                    res.append(copy.deepcopy(arr))
                return

            for i in range(len(nums)):
                if not fq[nums[i]]:
                    arr.append(nums[i])
                    fq[nums[i]] = 1
                    dfs(fq, arr, res)
                    arr.pop()
                    fq[nums[i]] = 0

            return res

        fq = dict.fromkeys(nums, 0)
        return dfs(fq, [], [])
    
# Method 3 - backtracking
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        ans = []

        def recursion(arr):
            if len(res) == len(arr):
                ans.append(copy.deepcopy(res))
                return

            for i in range(len(arr)):
                if used[i]:
                    continue
                res.append(arr[i])
                used[i] = True
                recursion(arr)
                res.pop()
                used[i] = False

            return ans

        return recursion(nums)
