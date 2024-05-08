class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stck = []

        for i in range(len(nums)):          
            while stck and stck[-1] > nums[i] and len(stck) - 1  + len(nums) - i >=k:
                stck.pop()
            stck.append(nums[i]) 

        if len(stck) > k:
            while len(stck) > k:
                stck.pop()                            

        return stck