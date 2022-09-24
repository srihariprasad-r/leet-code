class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(idx, arr, lst, res=[]):
            res.append(copy.deepcopy(lst))
            
            for j in range(idx, len(arr)):
                lst.append(arr[j])
                backtrack(j+1, arr, lst, res)
                lst.pop()
            
            return res
        
        curList = []
        ans = []
        
        return backtrack(0, nums, curList, ans)

# Method 2

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ans = []
        
        def dfs(cur, idx):
            if idx == n:
                ans.append(cur)
                return
            
            dfs(cur, idx+1)
            dfs(cur + [nums[idx]],idx + 1)
            
            return ans
        
        return dfs([], 0)

