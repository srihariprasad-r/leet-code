class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    
        for i in range(len(nums)):
            res = max(res, dp[i])
            
        return res

# TLE
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mx = float('-inf')
        ans = list()

        def increasing(l):
            if len(l) == 1: return True
            i = 0
            j = 1
            if l[i] > l[j]: return False
            while j < len(l):
                if l[i] > l[j]:
                    return False
                i += 1
                j += 1

            return True
            
        def recurse(idx,arr):
            if arr and arr not in ans: ans.append(arr[:])

            for i in range(idx, len(nums)):
                arr.append(nums[i])
                recurse(i+1,arr)
                arr.pop()
                # recurse(idx+1, arr)

            return ans

        ls = recurse(0, [])
        # print(ls)
        for l in ls:
            if increasing(l):
                mx = max(mx, len(set(l)))

        return mx