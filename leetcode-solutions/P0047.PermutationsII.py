# TLE

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        mp = {}
        res = list()
        fnl = list()
        
        for n in nums:
            if not(n in mp):
                mp[n] = 1
            else:
                mp[n] += 1
        

        def permutation(mp, nums, res=[], lvl=0):
            if lvl == len(nums):
                if res not in fnl:
                    fnl.append(res)
                # res = []
                return
                
            for i in range(len(nums)):
                if not mp[nums[i]]:
                    continue
                
                mp[nums[i]] -= 1
                permutation(mp, nums, res + [nums[i]], lvl+1)
                mp[nums[i]] += 1
                
            return fnl
        
        return permutation(mp, nums, res, 0)
                
# Method 2 - TLE

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        mp = {}
        res = list()
        fnl = list()
        
        nums.sort()

        for n in nums:
            if not(n in mp):
                mp[n] = 1
            else:
                mp[n] += 1
        

        def permutation(mp, nums, res=[], lvl=0):
            if lvl == len(nums):
                if res not in fnl:
                    fnl.append(res)
                # res = []
                return
                
            for i in range(len(nums)):
                if not mp[nums[i]]:
                    continue
                
                mp[nums[i]] -= 1
                permutation(mp, nums, res + [nums[i]], lvl+1)
                mp[nums[i]] += 1
                
            return fnl
        
        # return permutation(mp, nums, res, 0)
    
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            return permutation(mp, nums, res, i)

# Method 3 - TLE  

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(fq, arr, res):
            if len(arr) == len(nums):
                if arr not in res: res.append(copy.deepcopy(arr))
                return

            for num in nums:
                if fq[num]:
                    fq[num] -= 1
                    arr.append(num)
                    dfs(fq, arr, res)
                    arr.pop()
                    fq[num] += 1

            return res

        fq = Counter(nums)
        return dfs(fq, [],[])