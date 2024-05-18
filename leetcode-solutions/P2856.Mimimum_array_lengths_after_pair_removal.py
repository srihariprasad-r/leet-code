# wrong submission
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        j = len(nums) - 1
        i = j - 1
        ans = 0

        while i >= 0 and j >= 0:
            i = j - 1
            if nums[j] > nums[i]:
                j = i - 1
                i -= 1
                ans += 2
            else:
                j = i
                i -= 1
        
        return len(nums) - ans
    
# wrong submission
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        stck = []
        de = False
        
        stck.append(nums[0])
        for i in range(1,len(nums)-1):
            while stck and stck[-1] < nums[i]:
                stck.pop()
                de = True
            if de and stck: stck.pop()
            stck.append(nums[i])
        
        if stck and stck[-1] < nums[-1]: stck.pop()
        
        return len(stck)