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
                