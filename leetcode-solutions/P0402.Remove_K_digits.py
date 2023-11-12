class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        if len(nums) == 1 and k >=1: return '0'

        stck = [nums[0]]

        for i in range(1, len(nums)):
            while stck and int(stck[-1]) > int(nums[i]) and k > 0:
                stck.pop()
                k -= 1
            stck.append(nums[i])

        while stck and stck[0] == '0': stck.pop(0)

        res = ''.join(stck[:-k]) if k > 0 else ''.join(stck)

        return res  or '0'      

