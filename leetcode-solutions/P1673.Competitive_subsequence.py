# wrong submission
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stck = []

        for i in range(len(nums)):          
            while stck and stck[-1] > nums[i]:
                stck.pop()
            stck.append(nums[i]) 
                             
        while len(stck) > k:
            stck.pop()                            

        return stck